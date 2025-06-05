# ...existing code...

from datetime import date
from infraestructure.database import StoreDisabledDatesORM

class StoreDisabledDatesRepository:
    def __init__(self, session):
        self.session = session

    def get_dates_by_store_id(self, store_id: int):
        today = date.today()
        return [
            row.the_date
            for row in self.session.query(StoreDisabledDatesORM.the_date)
            .filter(StoreDisabledDatesORM.store_id == store_id,  StoreDisabledDatesORM.the_date > today)
            .all()
        ]