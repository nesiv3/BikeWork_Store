from sqlalchemy import Column, BigInteger, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_ltwZKMkt-uINKqDv49B@store-db-store-database-ds.g.aivencloud.com:15941/bikework_store"

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
