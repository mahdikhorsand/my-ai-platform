from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import secrets

router = APIRouter()

class RegisterRequest(BaseModel):
    name: str
    contact: str  # ایمیل یا شماره

class RegisterResponse(BaseModel):
    tenant_id: int
    api_key: str

@router.post("/register", response_model=RegisterResponse)
def register(request: RegisterRequest):
    # برای فاز 1 فقط داده‌ها را ذخیره نمی‌کنیم، فقط API key تولید می‌کنیم
    tenant_id = secrets.randbelow(1000)
    api_key = secrets.token_hex(16)
    return {"tenant_id": tenant_id, "api_key": api_key}

class LoginRequest(BaseModel):
    contact: str

class LoginResponse(BaseModel):
    message: str

@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest):
    # برای فاز 1 فقط پیام می‌دهیم
    return {"message": f"ورود موفق برای {request.contact}"}
