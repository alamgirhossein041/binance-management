from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    name: str
    is_active: Optional[bool] = True


class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    # wallets: list[Wallet] = []

    class Config:
        orm_mode = True