from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.database import get_db
from app.core.dependencies import get_current_user
from app.models.task import Task
from app.models.user import User
from app.models.project_member import ProjectMember   # IMPORTANT

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/")
def get_dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    #  FIX: Get ALL tasks from user's projects (NOT just assigned)
    tasks = (
        db.query(Task)
        .join(ProjectMember, ProjectMember.project_id == Task.project_id)
        .filter(ProjectMember.user_id == current_user.id)
        .all()
    )

    total = len(tasks)
    pending = len([t for t in tasks if t.status == "pending"])
    completed = len([t for t in tasks if t.status == "completed"])

    #  Overdue
    now = datetime.utcnow()
    overdue = len([
        t for t in tasks
        if t.due_date and t.due_date < now and t.status != "completed"
    ])

    #  Priority stats (safe check)
    high_priority = len([t for t in tasks if getattr(t, "priority", None) == "high"])
    medium_priority = len([t for t in tasks if getattr(t, "priority", None) == "medium"])
    low_priority = len([t for t in tasks if getattr(t, "priority", None) == "low"])

    return {
        "total_tasks": total,
        "pending": pending,
        "completed": completed,
        "overdue": overdue,
        "priority": {
            "high": high_priority,
            "medium": medium_priority,
            "low": low_priority
        }
    }