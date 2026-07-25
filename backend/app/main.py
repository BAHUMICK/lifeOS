from fastapi import FastAPI
from app.routers.auth import router as auth_router
from app.database.database import Base, engine
from app.models.user import User

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title = "lifeOS API",
    version = "1.0.0"
)
app.include_router(auth_router)

@app.get("/")
def home():
    return{
        "message":"welcome to lifeOS"
    }