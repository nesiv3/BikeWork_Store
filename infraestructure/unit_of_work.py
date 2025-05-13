from infraestructure.database import SessionLocal
from infraestructure.repositories.store_repositories import StoreRepository

class IUnitOfWork:
    def __enter__(self): ...
    def __exit__(self, *args): ...
    def commit(self): ...
    @property
    def stores(self): ...

class SqlAlchemyUnitOfWork(IUnitOfWork):
    def __init__(self):
        self.session = SessionLocal()
        self._stores = StoreRepository(self.session)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
        else:
            self.commit()
        self.session.close()

    def commit(self):
        self.session.commit()

    @property
    def stores(self):
        return self._stores
