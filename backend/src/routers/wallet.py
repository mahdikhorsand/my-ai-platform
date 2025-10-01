from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel

router = APIRouter()

class TopUpRequest(BaseModel):
    amount: float

class TopUpResponse(BaseModel):
    message: str
    balance: float

class TransactionsResponse(BaseModel):
    transactions: list

# موجودی کیف پول mock
mock_wallet_balance = 100.0
mock_transactions = []

@router.post("/topup", response_model=TopUpResponse)
def topup(request: TopUpRequest, x_tenant_apikey: str = Header(...)):
    global mock_wallet_balance, mock_transactions
    if not x_tenant_apikey:
        raise HTTPException(status_code=400, detail="API key required")
    mock_wallet_balance += request.amount
    mock_transactions.append({"type": "topup", "amount": request.amount})
    return {"message": f"شارژ موفق: {request.amount}", "balance": mock_wallet_balance}

@router.get("/transactions", response_model=TransactionsResponse)
def get_transactions(x_tenant_apikey: str = Header(...)):
    if not x_tenant_apikey:
        raise HTTPException(status_code=400, detail="API key required")
    return {"transactions": mock_transactions}
