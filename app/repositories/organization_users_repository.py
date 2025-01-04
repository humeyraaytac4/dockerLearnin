from fastapi import  HTTPException
# app/repositories/organization_user_repository.py
from sqlalchemy.orm import Session
from app.models import OrganizationUser
from app.schemas.organization_users_schemas import OrganizationUserCreate

class OrganizationUserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, org_user: OrganizationUserCreate) -> OrganizationUser:
        try:
            db_org_user = OrganizationUser(
            organization_id=org_user.organization_id,
            user_id=org_user.user_id
            )
            self.db.add(db_org_user)
            self.db.commit()
            self.db.refresh(db_org_user)
            return db_org_user
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete(self, id: int) -> str:
        try:
            org_user_to_delete = self.db.query(OrganizationUser).filter(OrganizationUser.id == id).first()
            if org_user_to_delete:
                self.db.delete(org_user_to_delete)
                self.db.commit()
                return f"OrganizationUser with id {id} has been deleted."
            else:
                return "OrganizationUser not found."
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))




