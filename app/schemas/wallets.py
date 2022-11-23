from typing import Optional
from pydantic import BaseModel

class WalletBase(BaseModel):
    owner_id: int
    is_active: Optional[bool] = True
    # coins: Optional[str]

class WalletCreate(WalletBase):
    api_key: str
    secret_key: str

class Wallet(BaseModel):
    id: int
    balance: Optional[str]

    class Config:
        orm_mode = True