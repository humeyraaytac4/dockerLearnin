from pydantic import BaseModel
from typing import Optional

class AddressBase(BaseModel):
    user_id: int
    city: str
    state: str
    postalcode: int
    country: str

    class Config:
        from_attributes=True



class AddressCreate(AddressBase):
    pass

class AddressUpdate(AddressBase):
    pass

class AddressResponse(AddressBase):
    id:int
    user_name: Optional[str] = None
    
    class Config:
        from_attributes=True
        
