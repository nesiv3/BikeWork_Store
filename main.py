from fastapi import FastAPI
from infraestructure.database import Base, engine
from api import store

from fastapi import FastAPI

app = FastAPI(
    title="BikeWork Store API",
    description="API para gestionar las tiendas de BikeWork.",
    version="1.0.0",
    contact={
        "name": "Soporte BikeWork",
        "email": "soporte@bikework.com",
    },
    license_info={
        "name": "DasavaNIV License",
        "url": "https://opensource.org/licenses/MIT",
    },
)



Base.metadata.create_all(bind=engine)

app.include_router(store.router, prefix="/api")
