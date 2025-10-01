from pydantic import BaseModel

class RegisterRequest(BaseModel):
    name: str
    contact: str

class TopupRequest(BaseModel):
    amount: float

class AskRequest(BaseModel):
    user_id: str
    prompt: str
