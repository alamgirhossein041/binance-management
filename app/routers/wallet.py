from app.crud import wallet as wallet_crud
from app.crud import user as user_crud
from app.schemas import wallets as wallet_schemas
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.helpers import deps

from binance.spot import Spot as Client
from binance.error import ClientError

import os
from dotenv import load_dotenv
load_dotenv()
BASE_URL = os.getenv('base_url')


router = APIRouter(
    prefix="/wallets",
    tags=["wallets"],
)

# Create new wallet for a user ID
@router.post("/create", response_model=wallet_schemas.Wallet)
def create_user(data: wallet_schemas.WalletCreate, db: Session = Depends(deps.get_db)):
    db_user = user_crud.get_user_by_id(db, user_id=data.owner_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User doesn't exist")

    client = Client(base_url=BASE_URL, key=data.api_key, secret=data.secret_key)
    try:
        r = client.account()
        print(r)
        data.balance = r["balances"]
    except ClientError as e:
        print(e.error_message)
    print(data)

    return wallet_crud.create_wallet(db=db, data=data)

# Return 1 wallet by ID
@router.get("/{wallet_id}", response_model=wallet_schemas.Wallet)
async def chack_balance(wallet_id: int = 0, db: Session = Depends(deps.get_db)) -> wallet_schemas.Wallet:
    wallet = wallet_crud.get_wallet_by_id(db, wallet_id=wallet_id)
    if not wallet:
        raise HTTPException(status_code=400, detail="Wallet doesn't exist")
    return wallet