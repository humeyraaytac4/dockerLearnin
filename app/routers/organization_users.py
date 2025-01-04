# app/routers/organization_users.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.organization_users_schemas import OrganizationUserCreate, OrganizationUserResponse
from app.repositories.organization_users_repository import OrganizationUserRepository
from app.dependencies import get_db
router = APIRouter()

@router.post("/",
            name='organization_users.post',
            dependencies=[],
            response_model=OrganizationUserResponse,
            tags=['organization_users post']
            )
def store(org_user: OrganizationUserCreate, db: Session = Depends(get_db)):
    repository = OrganizationUserRepository(db)
    return repository.create(org_user)





@router.delete("/{id}",
                name='organization_users.delete', 
                tags=['organization_users delete']
                )
def destroy(id: int, db: Session = Depends(get_db)):
    repository = OrganizationUserRepository(db)
    return repository.delete(id)
