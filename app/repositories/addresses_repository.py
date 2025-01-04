from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import Address
from app.schemas.addresses_schemas import AddressCreate, AddressUpdate, AddressResponse
from app.models import User,Address

def get_address_list(db: Session):
    try:
        # Tüm adresleri al
        addresses = db.query(Address).all()
        result = []

        for address in addresses:
            # Kullanıcıyı al
            user = db.query(User).filter(User.id == address.user_id).first()  # Kullanıcıyı al

            # Adres verilerini oluştur
            address_data = {
                "id": address.id,  # id ekleyin
                "user_id": address.user_id,
                "city": address.city,
                "state": address.state,
                "postalcode": address.postalcode,  # Burayı string'e çevirin
                "country": address.country,
                "user_name": f"{user.name} {user.surname}" if user else None  # Kullanıcı adı ve soyadı
            }
            result.append(address_data)

        return result
    finally:
        db.close()




def get_address_by_id(db: Session, id: int):
    try:
        # Belirtilen ID'ye göre adresi al
        address = db.query(Address).filter(Address.id == id).first()
        if address is None:
            raise HTTPException(status_code=404, detail="Address not found")
        
        # Kullanıcıyı al
        user = db.query(User).filter(User.id == address.user_id).first()  # Kullanıcıyı al

        # Adres verilerini oluştur
        address_data = {
            "id": address.id,
            "user_id": address.user_id,
            "city": address.city,
            "state": address.state,
            "postalcode": address.postalcode,  # Burayı string'e çevirin
            "country": address.country,
            "user_name": f"{user.name} {user.surname}" if user else None
        }

        return address_data  # Tek bir adres verisini döndür
    
    finally:
        db.close()



def store_address_list(db: Session, address: AddressCreate):
    try:
        db_address = Address(
            user_id=address.user_id,
            city=address.city,
            state=address.state,
            postalcode=address.postalcode,
            country=address.country
        )
        db.add(db_address)
        db.commit()
        db.refresh(db_address)

        # Sözlük olarak döndür
        return {
            "user_id": db_address.user_id,
            "city": db_address.city,
            "state": db_address.state,
            "postalcode": address.postalcode,  # Burayı string'e çevirin
            "country": db_address.country
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e)) 



def update_address(db: Session, id: int, address_update: AddressUpdate):
    # Belirtilen ID'ye göre adresi al
    address = db.query(Address).filter(Address.id == id).first()
    
    if address is None:
        raise HTTPException(status_code=404, detail="Address not found")

    # print(f"Incoming postalcode type: {type(address_update.postalcode)}, value: {address_update.postalcode}")
    # print("Updated address:", address)
    # Kullanıcı bilgilerini güncelle
    address.user_id = address_update.user_id
    address.city = address_update.city
    address.state = address_update.state
    address.postalcode = address_update.postalcode  # Burada tipin string olduğundan emin olun
    address.country = address_update.country
    print(address, flush=True)
    try:
        db.commit()  # Değişiklikleri kaydet
        db.refresh(address)  # Güncellenen adres verisini al
        return address
    except Exception as e:
        # db.rollback()  # Hata durumunda geri al
        # print(f"Update error: {e}")  # Hata detaylarını yazdır
        raise HTTPException(status_code=500, detail=str(e))  # Genel hata mesajı



def delete_address(db: Session, address_id: int):
    try:
        # Kullanıcıyı ID'sine göre bul ve sil
        address = get_address_by_id(db, address_id)
        if address:
            db.delete(address)
            db.commit()
            return {"message": f"Address with id {id} has been deleted."}
        else:
            return {"error": "Address not found."}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
    finally:
        db.close()   