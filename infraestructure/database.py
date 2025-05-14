import os  # Asegúrate de importar el módulo os
from sqlalchemy import TIMESTAMP, Column, BigInteger, Date, Double, Float, ForeignKey, Integer, String, create_engine
from sqlalchemy.types import Boolean
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

class StoreDisabledDatesORM(Base):
    __tablename__ = "store_disabled_dates"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    store_id = Column(BigInteger, ForeignKey("store.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    the_date = Column(Date, nullable=False)
    reason = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP, nullable=True)

class StoreSpecialDayPolicyORM(Base):
    __tablename__ = "store_special_day_policy"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    store_id = Column(BigInteger, ForeignKey("store.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    day_type = Column(String(10), nullable=False)
    is_operational = Column(Boolean, nullable=False)
    effective_date = Column(Date, nullable=False)
    end_date = Column(Date)
    created_at = Column(TIMESTAMP)

class StoreMaintenanceORM(Base):
    __tablename__ = "store_maintenance"

    id = Column(Integer, primary_key=True, autoincrement=True)
    store_id = Column(BigInteger, ForeignKey("store.id"), nullable=False)
    name = Column(String(100), nullable=False)
    cost = Column(Float, nullable=False)
    time = Column(Double, nullable=False)