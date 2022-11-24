from sqlalchemy.orm import Session
from app.models import models
from app.schemas import wallets

def get_wallet_by_user_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_wallet_by_id(db: Session, wallet_id: int):
    return db.query(models.Wallet).filter(models.Wallet.id == wallet_id).first()

def get_wallet_by_api_key(db: Session, api_key: str):
    return db.query(models.Wallet).filter(models.Wallet.api_key == api_key).first()

def get_all_wallets(db: Session):
    return db.query(models.Wallet).all()

def create_wallet(db: Session, data: wallets.WalletCreate):
    db_wallet = models.Wallet(owner_id = data.owner_id, api_key = data.api_key, secret_key = data.secret_key, balance = data.balance)
    db.add(db_wallet)
    db.commit()
    db.refresh(db_wallet)
    return db_wallet
