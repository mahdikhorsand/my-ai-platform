from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel

router = APIRouter()

class AskRequest(BaseModel):
    user_id: str
    prompt: str

class AskResponse(BaseModel):
    reply: str

@router.post("/ask", response_model=AskResponse)
def ask_endpoint(request: AskRequest, x_tenant_apikey: str = Header(...)):
    if not x_tenant_apikey:
        raise HTTPException(status_code=400, detail="API key required")
    # برای فاز 1 فقط پاسخ mock می‌دیم
    return {"reply": f"این پاسخ تستی برای: {request.prompt}"}
