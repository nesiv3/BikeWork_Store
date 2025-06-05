from infraestructure.database import StoreMaintenanceORM

class StoreMaintenanceRepository:
    def __init__(self, session):
        self.session = session

    def get_by_store_id(self, store_id: int):
        print(store_id)
        return (
            self.session.query(StoreMaintenanceORM)
            .filter(StoreMaintenanceORM.store_id == store_id)
            .all()
        )