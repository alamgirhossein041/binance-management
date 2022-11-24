from typing import Optional
from pydantic import BaseModel

class WalletBase(BaseModel):
    # id: int
    owner_id: int
    is_active: Optional[bool] = True
    balance: Optional[list]

class WalletCreate(WalletBase):
    api_key: str
    secret_key: str


class Wallet(BaseModel):
    id: int
    balance: Optional[list]
    class Config:
        orm_mode = True