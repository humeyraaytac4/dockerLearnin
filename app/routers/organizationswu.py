from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.organizationswu_schemas import OrganizationShow
from app.dependencies import get_db
from app.repositories.organizationswu_repository import OrganizationswuRepository

router = APIRouter()

@router.get("/{id}", 
            name='organizationwu.show', 
            dependencies=[Depends(get_db)], 
            response_model=OrganizationShow,
            tags=['organizationwu show id'])
async def show(id: int, db: Session = Depends(get_db)):
    repository = OrganizationswuRepository(db)
    return repository.get_organization_with_users(id)


