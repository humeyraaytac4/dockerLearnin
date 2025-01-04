from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_URL = "mysql://root:password@mysql:3306/project"  # Veritabanı bağlantı URL'si

# SQLAlchemy ayarları
engine = create_engine(DATABASE_URL, pool_size=30, max_overflow=60, pool_recycle=200, pool_pre_ping=True)
session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionLocal = scoped_session(session_factory)

