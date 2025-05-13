from application.store.dto import StoreCreateDTO, StoreReadDTO
from infraestructure.unit_of_work import IUnitOfWork
from domain.store import Store

class CreateStoreCommand:
    def __init__(self, data: StoreCreateDTO):
        self.data = data

class CreateStoreHandler:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    def handle(self, command: CreateStoreCommand) -> StoreReadDTO:
        store = Store(id=0, **command.data.dict())  # id se ignora, DB lo genera
        created = self.uow.stores.add(store)
        self.uow.commit()
        return StoreReadDTO.from_orm(created)
