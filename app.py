# app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI in Docker!"}



from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql://root:password@mysql:3306/project"  # Veritabanı bağlantı URL'si

# SQLAlchemy ayarları
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Model tanımı
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    surname = Column(String(100))

# Veritabanı tablolarını oluştur
Base.metadata.create_all(bind=engine)


class UserCreate(BaseModel):
    name: str
    surname: str

@app.post("/users")
def create_user(user: UserCreate):
    db = SessionLocal()
    try:
        db_user = User(name=user.name, surname=user.surname)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()  # Hata durumunda geri al
        return {"error": str(e)}
    finally:
        db.close()




# Tüm öğeleri almak için endpoint
@app.get("/users")
async def get_items():
    db = SessionLocal()
    db_users = db.query(User).all() #select * from table(model)
    return db_users


@app.get("/users/{id}")
async def get_user(id:int):
    db = SessionLocal()
    try:
        # Belirtilen ID'ye göre kullanıcıyı al
        user = db.query(User).filter(User.id == id).first()
        if user is None:
            return {"error": "User not found"}
        return user
    finally:
        db.close()


from fastapi import HTTPException

@app.put("/users/{id}")
async def update_user(id: int, user_update: UserCreate):
    db = SessionLocal()
    try:
        # Belirtilen ID'ye göre kullanıcıyı al
        user = db.query(User).filter(User.id == id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Kullanıcı bilgilerini güncelle
        user.name = user_update.name
        user.surname = user_update.surname
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        db.rollback()  # Hata durumunda geri al
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()


@app.delete("/users/{id}")
def delete_user(id: int):
    db = SessionLocal()
    try:
        # Kullanıcıyı ID'sine göre bul
        user_to_delete = db.query(User).filter(User.id == id).first()
        if user_to_delete:
            db.delete(user_to_delete)
            db.commit()
            return {"message": f"User with id {id} has been deleted."}
        else:
            return {"error": "User not found."}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
    finally:
        db.close()


