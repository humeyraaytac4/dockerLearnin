from sqlalchemy.orm import Session
from faker import Faker
from app.models import User, Address

fake = Faker()

def seed_addresses(db: Session, num_addresses: int = 10):
    """Rastgele adres verisi ekler."""
    user_ids = [user.id for user in db.query(User).all()]  # Mevcut kullanıcı ID'lerini al
    for _ in range(num_addresses):
        if user_ids:  # Eğer mevcut kullanıcı varsa
            address = Address(
                user_id=fake.random.choice(user_ids),  # Rastgele bir user_id seç
                city=fake.city(),
                state=fake.state(),
                postalcode=fake.random_int(min=10000, max=99999),
                country=fake.country()
            )
            db.add(address)

    db.commit()