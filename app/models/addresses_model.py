from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String

from app.models.base_model import Base

from pydantic import BaseModel

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer , ForeignKey("users.id")) 
    city = Column(String(100))
    state = Column(String(100))
    postalcode = Column(Integer)
    country = Column(String(100))


class AddressCreate(BaseModel):
    user_id: int
    city: str
    state: str
    postalcode: str
    country: str

