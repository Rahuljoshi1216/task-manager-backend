from sqlalchemy.orm import Session
from datetime import datetime

from app.models.task import Task
from app.models.project_member import ProjectMember


def get_dashboard_data(db: Session, user_id: int):
    # 🔥 Get all tasks from user's projects
    tasks = (
        db.query(Task)
        .join(ProjectMember, ProjectMember.project_id == Task.project_id)
        .filter(ProjectMember.user_id == user_id)
        .all()
    )

    total = len(tasks)
    pending = len([t for t in tasks if t.status == "pending"])
    completed = len([t for t in tasks if t.status == "completed"])

    now = datetime.utcnow()
    overdue = len([
        t for t in tasks
        if t.due_date and t.due_date < now and t.status != "completed"
    ])

    return {
        "total_tasks": total,
        "pending": pending,
        "completed": completed,
        "overdue": overdue
    }