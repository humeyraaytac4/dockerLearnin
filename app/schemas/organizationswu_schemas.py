from pydantic import BaseModel
from typing import List

class UserShow(BaseModel):
    id: int
    name: str
    surname: str

    class Config:
        from_attributes = True

class OrganizationShow(BaseModel):
    id: int
    name: str
    users: List[UserShow]

    class Config:
        from_attributes = True
