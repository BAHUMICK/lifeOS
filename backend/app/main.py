from fastapi import FastAPI
from app.routers.auth import router as auth_router
from app.routers.task import router as task_router
from app.routers.note import router as note_router
from app.database.database import Base, engine
from app.models.user import User
from app.models.task import Task
from app.models.note import Note

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title = "lifeOS API",
    version = "1.0.0"
)
app.include_router(auth_router)
app.include_router(task_router)
app.include_router(note_router)

@app.get("/")
def home():
    return{
        "message":"welcome to lifeOS"
    }

