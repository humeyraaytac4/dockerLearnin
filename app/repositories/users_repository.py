from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import User, Address
from app.schemas.users_schemas import UserCreate, UserUpdate

def get_user_list(db: Session):

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



def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user



def store_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, surname=user.surname)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        if user is None:
            return {"error": "User not found"}
        return db_user
    except Exception as e:
        db.rollback()  # Hata durumunda geri al
        return {"error": str(e)}




def update_user(db: Session, id: int, user_update: UserUpdate):
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
 



def delete_user(db: Session, id: int):
    user_to_delete = db.query(User).filter(User.id == id).first()
    try:
        # Kullanıcıyı ID'sine göre bul
        if user_to_delete:
            db.delete(user_to_delete)
            db.commit()
            return {"message": f"User with id {id} has been deleted."}
        else:
            return {"error": "User not found."}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}

