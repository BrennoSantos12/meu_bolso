from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str


class UserResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr


    class config:
        from_attributes = True

class UserUpdate(BaseModel):
    nome: Optional[str] = None 
    email: Optional[EmailStr] = None 



