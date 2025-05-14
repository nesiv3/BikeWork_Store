from infraestructure.database import StoreSpecialDayPolicyORM

class StoreSpecialDayPolicyRepository:
    def __init__(self, session):
        self.session = session

    def get_by_store_id(self, store_id: int):
        return (
            self.session.query(StoreSpecialDayPolicyORM)
            .filter(StoreSpecialDayPolicyORM.store_id == store_id)
            .all()
        )