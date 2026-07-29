from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.core.security import get_current_user

router = APIRouter()

@router.post("/tasks", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    new_task = Task(
        title = task.title,
        description = task.description,
        user_id = current_user.id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks(
    db :Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    tasks = db.query(Task).filter(Task.user_id == current_user.id).all()
    return tasks