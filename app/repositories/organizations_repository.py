# app/repositories/organization_repository.py
from sqlalchemy.orm import Session
from app.models.organizations_model import Organization
from app.schemas.organizations_schemas import OrganizationCreate



def create_organization(db: Session, organization: OrganizationCreate):
    try:
        db_organization = Organization(name=organization.name)
        db.add(db_organization)
        db.commit()
        db.refresh(db_organization)
        return db_organization
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



def get_organization_by_id(db: Session, id: int):
        organization= db.query(Organization).filter(Organization.id == id).first()
        if organization is None:
            raise HTTPException(status_code=404, detail="Organization not found")
        return organization



def get_organizations(db: Session):
    organizations = db.query(Organization).all()
    return organizations 



def update_organization(db: Session, id: int, organization_update: OrganizationCreate):
    organization = db.query(Organization).filter(Organization.id == id).first()
    if organization:
        organization.name = organization_update.name
        db.commit()
        db.refresh(organization)
        return organization
    else:
        return None


def delete_organization(db: Session, id: int):
    organization = db.query(Organization).filter(Organization.id == id).first()
    if organization:
        db.delete(organization)
        db.commit()
        return {"message": f"Organization with id {id} has been deleted."}
    else:
        return HTTPException(status_code=404, detail=result["error"])