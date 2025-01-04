# app/schemas/organization_user_schemas.py
from pydantic import BaseModel

class OrganizationUserCreate(BaseModel):
    organization_id: int
    user_id: int

class OrganizationUserResponse(BaseModel):
    id: int
    organization_id: int
    user_id: int

    class Config:
        orm_mode = True  # SQLAlchemy modelini kullanabilmek için orm_mode'u aktif hale getirin.
