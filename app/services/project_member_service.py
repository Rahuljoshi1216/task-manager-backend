from app.models.project_member import ProjectMember
from app.models.user import User


def add_member_service(db, project_id, user_id):
    #  check if user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"error": "User not found"}

    #  prevent duplicate member
    existing = db.query(ProjectMember).filter(
        ProjectMember.project_id == project_id,
        ProjectMember.user_id == user_id
    ).first()

    if existing:
        return {"error": "User already a member"}

    #  create member (default role = member)
    member = ProjectMember(
        project_id=project_id,
        user_id=user_id,
        role="member"
    )

    db.add(member)
    db.commit()
    db.refresh(member)

    return member