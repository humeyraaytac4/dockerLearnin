from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.repositories.users_repository import get_user_list, get_user_by_id, store_user, update_user, delete_user
from app.schemas.users_schemas import UserCreate, UserUpdate, UserResponse
from app.dependencies import get_db
from typing import List

router = APIRouter()

@router.post("/",
            name='users.post',
            dependencies=[],
            response_model=UserResponse,
            tags=['users post']
            )
def store(user: UserCreate, db: Session = Depends(get_db)):
    return store_user(db, user)



@router.get("/{id}", 
            name='users.show', 
            dependencies=[Depends(get_db)], 
            response_model=UserResponse,
            tags=['users show id'])
def show(id: int, db: Session = Depends(get_db)):
    return get_user_by_id(db, id)



@router.put("/{id}", 
            name='users.update', 
            dependencies=[Depends(get_db)], 
            response_model=UserResponse, 
            tags=['users update'])
def update(id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, id, user_update)



@router.delete("/{id}",
                name='users.delete', 
                tags=['users delete']
                )
def destroy(id: int, db: Session = Depends(get_db)):
    return delete_user(db, id)



@router.get("/",
            name='users.get',
            dependencies=[],
            response_model=List[UserResponse],
            tags=['users get']
            )
def index(db: Session = Depends(get_db)):
    return get_user_list(db)

