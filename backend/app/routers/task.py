from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.core.security import get_current_user

def get_task_or_404(
        task_id : int,
        db: Session ,
        current_user 
):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code= 404,
            detail= "task not found"
        )
    if task.user_id != current_user.id:
        raise HTTPException(
            status_code= 403,
            detail= "Not authorized"
        )
    return task 

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

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(
    task_id : int,
    db :Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    task = get_task_or_404(task_id, db, current_user)
    return task

@router.put("/tasks/{task_id}",response_model=TaskResponse)
def update_task(
    task_id : int,
    task_data: TaskUpdate,
    db : Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    task = get_task_or_404(task_id, db, current_user)
   
    task.title = task_data.title
    task.description = task_data.description
    task.completed = task_data.completed
    db.commit()
    db.refresh(task)
    return task

@router.delete("/tasks/{task_id}", response_model=TaskResponse)
def delete_task(
    task_id : int,
    db : Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    task = get_task_or_404(task_id, db, current_user)
    db.delete(task)
    db.commit()
    return task