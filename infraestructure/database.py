import os  # Asegúrate de importar el módulo os
from sqlalchemy import Column, BigInteger, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


# Cargar variables de entorno desde el archivo .env
load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class StoreORM(Base):
    __tablename__ = "store"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(255))
    address = Column(String(255))
    document_type = Column(String(10))
    document_number = Column(String(50))
    phone_number = Column(String(50))
    image = Column(String(255))
