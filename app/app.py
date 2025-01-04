# sudo docker compose up -d --build
# app.py
from fastapi import FastAPI
#from app.models.base_model import Base
#from app.config.database import engine
# Route dosyalarını import et
from app.routers import users, addresses, organizations, organization_users, userswo,organizationswu,seeders

app = FastAPI()
# Base.metadata.create_all(bind=engine)


# Router'ları FastAPI uygulamasına ekle
app.include_router(users.router, prefix="/users")
app.include_router(addresses.router, prefix="/addresses")
app.include_router(organizations.router, prefix="/organizations")
app.include_router(organization_users.router, prefix="/organization_users")
app.include_router(userswo.router, prefix="/userswo")
app.include_router(organizationswu.router, prefix="/organizationswu")
app.include_router(seeders.router, prefix="/seeders")


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI in Docker!"}



