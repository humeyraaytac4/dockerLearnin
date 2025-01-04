from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String

from app.models.base_model import Base

from pydantic import BaseModel

# Model tanımı
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    surname = Column(String(100))

     # User ve Address arasında bir ilişki
    addresses= relationship("Address", backref="users")

    #User ve Organization arasındaki ilişki için
    organizations = relationship("Organization", secondary="organization_users", back_populates="users")



class UserCreate(BaseModel):
    name: str
    surname: str


