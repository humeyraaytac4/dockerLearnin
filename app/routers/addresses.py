from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Address ,User
from app.config.database import  SessionLocal
from app.dependencies import get_db
from app.schemas.addresses_schemas import AddressResponse, AddressUpdate, AddressCreate
from app.repositories.addresses_repository import store_address_list, get_address_by_id, get_address_list,update_address,delete_address
from typing import List

router = APIRouter()

@router.post("/",
            name='addresses.post',
            dependencies=[],
            tags=['addresses post'],
            response_model=AddressCreate
            )
def store(address: AddressCreate, db: Session = Depends(get_db)):
    return store_address_list(db, address)




@router.get("/{id}", 
            name='addresses.show', 
            dependencies=[Depends(get_db)], 
            response_model=AddressResponse,
            tags=['addresses show id'])
def show(id, db: Session = Depends(get_db)):
    return get_address_by_id(db, id)



@router.put("/{id}", 
            name='addresses.update', 
            dependencies=[Depends(get_db)], 
            tags=['addresses update'])
def update(id, request: AddressUpdate, db: Session = Depends(get_db)):
    return update_address(db,id, request, )



@router.delete("/{id}",
                name='addresses.delete', 
                tags=['addresses delete']
                )
def destroy(id, db: Session = Depends(get_db)):
    return delete_address(db, id)



@router.get("/",
            name='addresses.get',
            dependencies=[],
            response_model=List[AddressResponse],
            tags=['addresses get']
            )
def index(db: Session = Depends(get_db)):
    return get_address_list(db)