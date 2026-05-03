from pydantic import BaseModel

class AddMember(BaseModel):
    user_id: int