from sqlalchemy.orm import Session
from app.models import User

class UserWORepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_with_organizations(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
