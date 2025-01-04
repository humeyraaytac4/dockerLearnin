
from pydantic import BaseModel
from typing import Optional, List

class UserBase(BaseModel):
    name: str
    surname: str

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class AddressResponse(BaseModel):
    city: str
    state: str
    postalcode: int
    country: str

class UserResponse(UserBase):
    id: int
    addresses: Optional[List[AddressResponse]] = []

    class Config:
        from_attributes = True
