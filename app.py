# sudo docker compose up -d --build
# app.py
from fastapi import FastAPI
from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey



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

     # User ve Address arasında bir ilişki
    addressvuser= relationship("Address", backref="user")

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




# # Tüm öğeleri almak için endpoint
# @app.get("/users")
# async def get_items():
#     db = SessionLocal()
#     db_users = db.query(User).all() #select * from table(model)
#     return db_users



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


#Second Model
class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer , ForeignKey("users.id")) 
    city = Column(String(100))
    state = Column(String(100))
    postalcode = Column(Integer)
    country = Column(String(100))

# # Tabloları sil
# Base.metadata.drop_all(bind=engine)

# Veritabanı tablolarını oluştur
Base.metadata.create_all(bind=engine)

class AddressCreate(BaseModel):
    user_id: int
    city: str
    state: str
    postalcode: int
    country: str

@app.post("/addresses")
def create_address(address: AddressCreate):
    db = SessionLocal()
    try:
        db_address= Address(user_id=address.user_id, city=address.city, state=address.state, postalcode=address.postalcode, country=address.country)
        db.add(db_address)
        db.commit()
        db.refresh(db_address)
        return db_address
    except Exception as e:
        db.rollback()  # Hata durumunda geri al
        return {"error": str(e)}
    finally:
        db.close()

""" Tüm öğeleri almak için endpoint
@app.get("/addresses")
async def get_adresses():
    db = SessionLocal()
    db_addresses = db.query(Address).all() #select * from table(model)
    return db_addresses
 """

@app.get("/addresses/{id}")
async def get_address(id:int):
    db = SessionLocal()
    try:
        # Belirtilen ID'ye göre kullanıcıyı al
        address = db.query(Address).filter(Address.id == id).first()
        if address is None:
            return {"error": "User not found"}
        return address
    finally:
        db.close()

    s
@app.put("/addresses/{id}")
async def update_address(id: int, address_update: AddressCreate):
    db = SessionLocal()
    try:
        # Belirtilen ID'ye göre kullanıcıyı al
        address = db.query(Address).filter(Address.id == id).first()
        if address is None:
            raise HTTPException(status_code=404, detail="Address not found")
        
        # Kullanıcı bilgilerini güncelle
        address.user_id = address_update.user_id
        address.city = address_update.city
        address.state = address_update.state
        address.postalcode = address_update.postalcode
        address.country = address_update.country

        db.commit()
        db.refresh(address)
        return address
    except Exception as e:
        db.rollback()  # Hata durumunda geri al
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()



@app.delete("/addresses/{id}")
def delete_address(id: int):
    db = SessionLocal()
    try:
        # Kullanıcıyı ID'sine göre bul ve sil
        address_to_delete = db.query(Address).filter(Address.id == id).first()
        if address_to_delete:
            db.delete(address_to_delete)
            db.commit()
            return {"message": f"Address with id {id} has been deleted."}
        else:
            return {"error": "Address not found."}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
    finally:
        db.close()


# /users ile userları addresleriyle birlikte getirme
@app.get("/users")
async def get_users():
    db = SessionLocal()
    try:
        # Kullanıcıları ve ilişkili adreslerini al
        users = db.query(User).all()  # Tüm kullanıcıları al
        result = []
        for user in users:
            user_data = {
                "id": user.id,
                "name": user.name,
                "surname": user.surname,
                "addresses": []
            }
            # Kullanıcının sadece kendi adreslerini al ve ekle
            addresses = db.query(Address).filter(Address.user_id == user.id).all()
            for address in addresses:
                user_data["addresses"].append({
                    "city": address.city,
                    "state": address.state,
                    "postalcode": address.postalcode,
                    "country": address.country
                })
            result.append(user_data)
        return result
    finally:
        db.close()

 #users ile userları addresleriyle birlikte getirme
@app.get("/addresses")
async def get_addresses():
    db = SessionLocal()
    try:
        # Tüm adresleri al
        addresses = db.query(Address).all()
        result = []

        for address in addresses:
            # Kullanıcıyı al
            user = db.query(User).filter(User.id == address.user_id).first()  # Kullanıcıyı al

            # Adres verilerini oluştur
            address_data = {
                "user_id": address.user_id,
                "city": address.city,
                "state": address.state,
                "postalcode": address.postalcode,
                "country": address.country,
                "user_name": f"{user.name} {user.surname}" if user else None  # Kullanıcı adı ve soyadı
            }
            result.append(address_data)

        return result
    finally:
        db.close()


