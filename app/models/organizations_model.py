from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

from app.models.base_model import Base

from pydantic import BaseModel

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))

    users = relationship("User", secondary="organization_users", back_populates="organizations")



class OrganizationCreate(BaseModel):
    name: str

