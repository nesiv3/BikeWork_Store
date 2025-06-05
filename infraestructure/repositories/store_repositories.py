from domain.store import Store
from infraestructure.database import StoreORM
from sqlalchemy.orm import Session

class StoreRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, store: Store):
        store_orm = StoreORM(**store.__dict__)
        self.session.add(store_orm)
        self.session.flush()  # obtener ID
        return store_orm

    def get_by_id(self, store_id: int):
        return self.session.query(StoreORM).filter(StoreORM.id == store_id).first()
    
    def get_all(self):
        return self.session.query(StoreORM).all()
