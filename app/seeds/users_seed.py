from sqlalchemy.orm import Session
from faker import Faker
from app.models import User

fake = Faker()

def seed_users(db: Session, num_users: int = 10):
    """Rastgele kullanıcı verisi ekler."""
    
    for _ in range(num_users):
        user = User(
            name=fake.first_name(),
            surname=fake.last_name(),
        )
        db.add(user)
        db.commit()
        db.refresh(user)