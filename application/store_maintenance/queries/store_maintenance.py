from typing import List
from application.store_maintenance.dto import StoreMaintenanceDTO

class GetStoreMaintenanceQuery:
    def __init__(self, store_id: int):
        self.store_id = store_id

class GetStoreMaintenanceQueryHandler:
    def __init__(self, uow):
        self.uow = uow

    def handle(self, query: GetStoreMaintenanceQuery) -> List[StoreMaintenanceDTO]:
        print(query.store_id)
        maintenances = self.uow.store_maintenance.get_by_store_id(query.store_id)
        return [StoreMaintenanceDTO.model_validate(m) for m in maintenances]