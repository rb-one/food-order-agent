from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.model.auth.types.user import UserCreate, UserLogin
from app.repositories.orm.user import User
from app.utils.auth import hash_password, verify_password
from app.utils.db import get_db
from app.utils.jwt_handler import create_jwt

router = APIRouter()


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(user.password)
    print(user)
    new_user = User(username=user.username, email=user.email, password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    return {"message": "User registered successfully!"}


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    app_user = db.query(User).filter(User.username == user.username).first()
    if not app_user or not verify_password(user.password, app_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_jwt({"user": app_user.username})
    return {"token": token}
