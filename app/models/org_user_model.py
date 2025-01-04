from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String

from app.models.base_model import Base

from pydantic import BaseModel

# Model tanımı
class OrganizationUser(Base):
    __tablename__ = "organization_users"

    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

      # Organization ve User arasında bir ilişki
    user = relationship("User", overlaps="organizations,organization_users")
    organization = relationship("Organization", overlaps="users,organization_users")



class OrganizationUserCreate(BaseModel):
    organization_id:int
    user_id:int
