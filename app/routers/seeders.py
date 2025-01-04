from fastapi import APIRouter
from app.config.database import SessionLocal  # Veritabanı oturumu

from app.seeds.users_seed import seed_users
from app.seeds.addresses_seed import seed_addresses

router = APIRouter()

@router.get("/users")
def seeds():
    db = SessionLocal()
    try:
        seed_users(db, num_users=10)  # 100 kullanıcı ekle
    finally:
        db.close()
    return  bool()

@router.get("/addresses")
def seeds():
    db = SessionLocal()
    try:
        seed_addresses(db, num_addresses=10)  # 100 adres ekle
    finally:
        db.close()
    return  bool()


    