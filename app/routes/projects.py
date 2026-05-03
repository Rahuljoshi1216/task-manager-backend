from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.project import ProjectCreate
from app.schemas.project_member import AddMember
from app.services.project_service import (
    create_project_service,
    get_projects_service,
    get_project_by_id_service
)
from app.services.project_member_service import add_member_service
from app.core.dependencies import get_current_user
from app.models.user import User
from app.models.project import Project
from app.models.project_member import ProjectMember
from app.utils.permission import is_admin, is_project_member

router = APIRouter(prefix="/projects", tags=["Projects"])


# 🔹 CREATE PROJECT
@router.post("/")
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_project_service(db, project, current_user.id)


# 🔹 GET USER PROJECTS
@router.get("/")
def get_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_projects_service(db, current_user.id)


# 🔥 NEW: GET SINGLE PROJECT
@router.get("/{project_id}")
def get_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project = get_project_by_id_service(db, project_id)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if not is_project_member(db, project_id, current_user.id):
        raise HTTPException(status_code=403, detail="Access denied")

    return project


# 🔥 NEW: GET PROJECT MEMBERS (IMPORTANT FOR FRONTEND)
@router.get("/{project_id}/members")
def get_project_members(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not is_project_member(db, project_id, current_user.id):
        raise HTTPException(status_code=403, detail="Access denied")

    members = (
        db.query(User)
        .join(ProjectMember, ProjectMember.user_id == User.id)
        .filter(ProjectMember.project_id == project_id)
        .all()
    )

    return [
        {
            "id": m.id,
            "email": m.email
        }
        for m in members
    ]


# 🔥 ADD MEMBER (ADMIN ONLY)
@router.post("/{project_id}/add-member")
def add_member(
    project_id: int,
    member: AddMember,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project = get_project_by_id_service(db, project_id)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # 🔐 Only admin can add members
    if not is_admin(db, project_id, current_user.id):
        raise HTTPException(status_code=403, detail="Not allowed")

    return add_member_service(db, project_id, member.user_id)