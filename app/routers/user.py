from app import schemas
from app.crud import user as user_crud
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import Any, List
from app.helpers import deps

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

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
    return users

# Return user by ID
@router.get("/{user_id}", response_model=schemas.users.User)
def read_user(user_id: int = 0, db: Session = Depends(deps.get_db)) -> Any:
    user = user_crud.get_user_by_id(db, user_id)
    return user