from app.config.database import SessionLocal

def get_db():
    global db
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
