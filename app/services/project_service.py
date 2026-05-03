from app.models.project import Project
from app.models.project_member import ProjectMember


# 🔹 CREATE PROJECT
def create_project_service(db, project, user_id):
    new_project = Project(
        name=project.name,
        description=project.description,
        owner_id=user_id
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


# 🔹 GET PROJECT BY ID (FIX FOR YOUR ERROR)
def get_project_by_id_service(db, project_id):
    return db.query(Project).filter(Project.id == project_id).first()


# 🔹 GET PROJECTS (OWNER + MEMBER)
def get_projects_service(db, user_id):
    # projects where user is owner
    owned_projects = db.query(Project).filter(Project.owner_id == user_id)

    # projects where user is member
    member_projects = (
        db.query(Project)
        .join(ProjectMember, Project.id == ProjectMember.project_id)
        .filter(ProjectMember.user_id == user_id)
    )

    # combine both
    return owned_projects.union(member_projects).all()