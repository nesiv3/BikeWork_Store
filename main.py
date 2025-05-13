from fastapi import FastAPI
from infraestructure.database import Base, engine
from api import store

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(store.router, prefix="/api")
