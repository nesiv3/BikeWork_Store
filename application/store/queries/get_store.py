from infraestructure.unit_of_work import IUnitOfWork
from utils.exceptions import NotFoundException
from application.store.dto import StoreReadDTO

class GetStoreQuery:
    def __init__(self, store_id: int):
        self.store_id = store_id

class GetStoreQueryHandler:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    def handle(self, query: GetStoreQuery) -> StoreReadDTO:
        store = self.uow.stores.get_by_id(query.store_id)
        if not store:
            raise NotFoundException("Store")
        return StoreReadDTO.from_orm(store)
    
class GetAllStoresQuery:
    pass

class GetAllStoresQueryHandler:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    def handle(self, query: GetAllStoresQuery) -> list[StoreReadDTO]:
        stores = self.uow.stores.get_all()
        return [StoreReadDTO.from_orm(store) for store in stores]
