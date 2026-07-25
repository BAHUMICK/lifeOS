from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserRegister
from app.schemas.user import UserLogin
from app.models.user import User
from app.database.dependencies import get_db

from app.core.security import hash_password, verify_password

router = APIRouter()

@router.post("/register")

def register(user: UserRegister, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code= 400,
            detail = "email already exists"
        )
    new_user = User(
        username = user.username,
        email = user.email,
        password = hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return{
        "message":"user registered successfully",
        "user": {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email

        }
    }

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if  not existing_user:
        raise HTTPException(
                    status_code= 400,
                    detail = "invalid email or password"
        )
    if not verify_password(user.password, existing_user.password):
        raise HTTPException(
            status_code=400,
            detail=" invalid email or password"
        )
    return {
        "message":"login successfull"
    }