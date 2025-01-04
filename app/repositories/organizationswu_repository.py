# app/repositories/organization_user_repository.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import Organization
from app.schemas.organizationswu_schemas import OrganizationShow

class OrganizationswuRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_organization_with_users(self, id: int) -> OrganizationShow:
        organization = self.db.query(Organization).filter(Organization.id == id).first()
        if not organization:
            raise HTTPException(status_code=404, detail="Organization not found")
        
        users = [{"id": user.id, "name": user.name, "surname": user.surname} for user in organization.users]
        
        return {
            "id": organization.id,
            "name": organization.name,
            "users": users
        }

