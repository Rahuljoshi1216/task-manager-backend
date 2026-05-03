from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    description = Column(String(255))
    owner_id = Column(Integer, ForeignKey("users.id"))