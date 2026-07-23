from fastapi import APIRouter
from app.schemas.user import UserRegister

router = APIRouter()

@router.post("/register")

def register(user: UserRegister):
    return{
        "message":"User registered successfully",
        "user":user
    }