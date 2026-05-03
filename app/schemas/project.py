from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    description: str


class ProjectOut(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True