from app import schemas
from app.crud import user as user_crud
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import Any
from app.helpers import deps
from binance.spot import Spot as Client

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

import os
from dotenv import load_dotenv
load_dotenv()
BASE_URL = os.getenv('base_url')

# Create user
@router.post("/create", response_model=schemas.users.User)
def create_user(user: schemas.users.UserCreate, db: Session = Depends(deps.get_db)):
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db=db, data=user)

# Return all users
@router.get("/list", response_model=list[schemas.users.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)) -> Any:
    users = user_crud.get_all_users(db, skip=skip, limit=limit)
    if not users:
        raise HTTPException(status_code=400, detail="User doesn't exist")

    # Get all assets on users accounts and gets its prices
    for user in users:
        for wallet in user.wallets:
            if not wallet.balance:
                continue
            
            client = Client(base_url=BASE_URL, key=wallet.api_key, secret=wallet.secret_key)
            for coin in wallet.balance:
                if coin['asset'] in ["USDT", "BUSD"]:
                    coin['total'] = float(coin['free']) + float(coin['locked'])
                else:
                    price = client.ticker_price(symbol=coin['asset']+"USDT")['price']
                    coin['total'] = (float(coin['free']) + float(coin['locked'])) * float(price)

    return users