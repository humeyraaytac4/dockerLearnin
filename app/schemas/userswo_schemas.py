from pydantic import BaseModel
from typing import List

class OrganizationShow(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True  # SQLAlchemy nesnelerinden veri almak için

class UserShow(BaseModel):
    id: int
    name: str
    surname: str
    organizations: List[OrganizationShow]

    class Config:
        from_attributes = True  # SQLAlchemy nesnelerinden veri almak için
