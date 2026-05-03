from sqlalchemy import Column, Integer, ForeignKey, String
from app.db.base import Base

class ProjectMember(Base):
    __tablename__ = "project_members"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))

    #  ADD THIS
    role = Column(String(50), default="member")  # admin / member