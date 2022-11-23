from app.crud import wallet as wallet_crud
from app.crud import user as user_crud
from app.schemas import wallets as wallet_schemas
from app.schemas import users as users_schemas
from app.models import models
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import Any, List
from app.helpers import deps

router = APIRouter(
    prefix="/wallets",
    tags=["wallets"],
)

# Create new wallet for a user
@router.post("/create", response_model=wallet_schemas.Wallet)
def create_user(data: wallet_schemas.WalletCreate, db: Session = Depends(deps.get_db)):
    db_user = user_crud.get_user_by_id(db, user_id=data.owner_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User doesn't exist")

    db_api_key = wallet_crud.get_wallet_by_api_key(db, api_key=data.api_key)
    if db_api_key:
        raise HTTPException(status_code=400, detail="wallet already registered")

    return wallet_crud.create_wallet(db=db, data=data)

# Return all wallets
@router.get("/list", response_model=List[wallet_schemas.Wallet])
async def get_wallet_list(skip: int = 0, limit: int = 10, db: Session = Depends(deps.get_db)) -> List:
    return wallet_crud.get_all_wallets(db, skip=skip, limit=limit)
