from infraestructure.database import SessionLocal
from infraestructure.repositories.store_disabled_dates_repository import StoreDisabledDatesRepository
from infraestructure.repositories.store_repositories import StoreRepository
from infraestructure.repositories.store_special_day_policy_repository import StoreSpecialDayPolicyRepository

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
        self._store_disabled_dates = StoreDisabledDatesRepository(self.session)
        self._store_special_day_policy = StoreSpecialDayPolicyRepository(self.session)

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
    

    @property
    def store_disabled_dates(self):
        return self._store_disabled_dates

    @property
    def store_special_day_policy(self):
        return self._store_special_day_policy
