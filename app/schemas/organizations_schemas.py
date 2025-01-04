# app/schemas/organization_schemas.py
from pydantic import BaseModel
from typing import List

class OrganizationCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True

class OrganizationResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class OrganizationListResponse(BaseModel):
    organizations: List[OrganizationResponse]
