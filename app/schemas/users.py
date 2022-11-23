from typing import Optional
from pydantic import BaseModel
from app.schemas.wallets import Wallet

class UserBase(BaseModel):
    email: str
    name: str
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    pass

class User(BaseModel):
    id: int
    wallets: list[Wallet] = []

    class Config:
        orm_mode = True