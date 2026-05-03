from app.models.project import Project
from app.models.project_member import ProjectMember


#  Check if user is part of project
def is_project_member(db, project_id, user_id):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        return False

    # owner
    if project.owner_id == user_id:
        return True

    # member
    member = db.query(ProjectMember).filter(
        ProjectMember.project_id == project_id,
        ProjectMember.user_id == user_id
    ).first()

    return member is not None


#  Check if user is admin
def is_admin(db, project_id, user_id):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        return False

    # owner is always admin
    if project.owner_id == user_id:
        return True

    # admin member
    member = db.query(ProjectMember).filter(
        ProjectMember.project_id == project_id,
        ProjectMember.user_id == user_id,
        ProjectMember.role == "admin"
    ).first()

    return member is not None