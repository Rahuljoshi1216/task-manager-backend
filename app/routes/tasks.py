from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.task import TaskCreate, TaskUpdate
from app.services.task_service import (
    create_task_service,
    get_tasks_service,
    update_task_status_service
)
from app.core.dependencies import get_current_user
from app.models.user import User
from app.models.task import Task
from app.utils.permission import is_project_member

router = APIRouter(prefix="/tasks", tags=["Tasks"])


# 🔹 CREATE TASK (SECURE)
@router.post("/")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not is_project_member(db, task.project_id, current_user.id):
        raise HTTPException(status_code=403, detail="Access denied")

    return create_task_service(db, task)


# 🔹 GET ALL TASKS (USER BASED)
@router.get("/")
def get_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_tasks_service(db, current_user.id)


# 🔥 NEW: GET TASKS BY PROJECT (IMPORTANT)
@router.get("/{project_id}")
def get_tasks_by_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # 🔐 Access check
    if not is_project_member(db, project_id, current_user.id):
        raise HTTPException(status_code=403, detail="Access denied")

    tasks = db.query(Task).filter(Task.project_id == project_id).all()
    return tasks


# 🔹 UPDATE TASK STATUS (SECURE)
@router.put("/{task_id}")
def update_task_status(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    existing_task = db.query(Task).filter(Task.id == task_id).first()

    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")

    if not is_project_member(db, existing_task.project_id, current_user.id):
        raise HTTPException(status_code=403, detail="Access denied")

    return update_task_status_service(db, task_id, task.status)