from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.userswo_schemas import UserShow
from app.dependencies import get_db
from app.repositories.userswo_repository import UserWORepository

router = APIRouter()


@router.get("/{id}", 
            name='userswo.show', 
            response_model=UserShow,
            tags=['userswo show id'])
async def show(id: int, db: Session = Depends(get_db)):
    repository = UserWORepository(db)
    return repository.get_user_with_organizations(id)
    




