from fastapi import FastAPI, HTTPException, Header, Depends
from sqlalchemy.orm import Session
from config import engine, SessionLocal
from models import Base, Tenant, Wallet, Transaction
from schemas import RegisterRequest, TopupRequest, AskRequest
import uuid

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.post("/auth/register")
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    api_key = str(uuid.uuid4().hex)
    tenant = Tenant(name=request.name, contact=request.contact, api_key=api_key)
    wallet = Wallet(balance=0, tenant=tenant)
    db.add(tenant)
    db.add(wallet)
    db.commit()
    db.refresh(tenant)
    return {"tenant_id": tenant.id, "api_key": tenant.api_key}

@app.post("/wallet/topup")
def topup(request: TopupRequest, x_tenant_apikey: str = Header(...), db: Session = Depends(get_db)):
    tenant = db.query(Tenant).filter(Tenant.api_key == x_tenant_apikey).first()
    if not tenant:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    tenant.wallet.balance += request.amount
    transaction = Transaction(wallet=tenant.wallet, amount=request.amount, type="topup")
    db.add(transaction)
    db.commit()
    return {"message": f"شارژ موفق: {request.amount}", "balance": tenant.wallet.balance}

@app.post("/api/ask")
def ask(request: AskRequest, x_tenant_apikey: str = Header(...), db: Session = Depends(get_db)):
    tenant = db.query(Tenant).filter(Tenant.api_key == x_tenant_apikey).first()
    if not tenant:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    cost = 1
    if tenant.wallet.balance < cost:
        raise HTTPException(status_code=400, detail="موجودی کافی نیست")
    tenant.wallet.balance -= cost
    transaction = Transaction(wallet=tenant.wallet, amount=cost, type="ask")
    db.add(transaction)
    db.commit()
    return {"reply": f"این پاسخ تستی برای: {request.prompt}"}
