from sqlalchemy.orm import Session
# from typing import Optional

from app.models import models
from app.schemas import users

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, data: users.UserCreate):
    db_user = models.User(email=data.email, name=data.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
