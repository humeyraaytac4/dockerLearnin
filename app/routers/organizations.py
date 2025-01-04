# app/routers/organization_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.organizations_schemas import OrganizationCreate, OrganizationResponse
from app.repositories.organizations_repository import create_organization, get_organization_by_id, get_organizations, update_organization, delete_organization
from app.dependencies import get_db
from typing import List

router = APIRouter()


@router.post("/",
            name='organizations.post',
            dependencies=[],
            response_model=OrganizationResponse,
            tags=['organizations post']
            )
def store(organization: OrganizationCreate, db: Session = Depends(get_db)):
    return create_organization(db=db, organization=organization)



@router.get("/",
            name='organizations.get',
            dependencies=[],
            response_model=List[OrganizationResponse],
            tags=['organizations get']
            )
async def index(db: Session = Depends(get_db)):
    return get_organizations(db=db)



@router.get("/{id}", 
            name='organizations.show', 
            dependencies=[Depends(get_db)], 
            response_model=OrganizationResponse,
            tags=['organizations show id'])
async def show(id: int, db: Session = Depends(get_db)):
    return get_organization_by_id(db, id)



@router.put("/{id}", 
            name='organizations.update', 
            dependencies=[Depends(get_db)], 
            tags=['organizations update'])
async def update(id: int, organization_update: OrganizationCreate, db: Session = Depends(get_db)):
    return update_organization(db, id=id, organization_update=organization_update)



@router.delete("/{id}",
                name='addresses.delete', 
                tags=['addresses delete']
                )
def destroy(id: int, db: Session = Depends(get_db)):
    return delete_organization(db, id=id)
