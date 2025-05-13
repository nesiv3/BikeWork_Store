from fastapi import APIRouter, Depends, HTTPException
from application.store.queries.get_store import GetAllStoresQuery, GetAllStoresQueryHandler, GetStoreQuery, GetStoreQueryHandler
from infraestructure.unit_of_work import SqlAlchemyUnitOfWork
from application.store.commands.create_store import CreateStoreCommand, CreateStoreHandler
from application.store.dto import StoreCreateDTO, StoreReadDTO
from utils.exceptions import NotFoundException

router = APIRouter()

@router.post("/stores", response_model=StoreReadDTO)
def create_store(data: StoreCreateDTO):
    with SqlAlchemyUnitOfWork() as uow:
        handler = CreateStoreHandler(uow)
        return handler.handle(CreateStoreCommand(data))



@router.get("/stores/{store_id}", response_model=StoreReadDTO)
def get_store(store_id: int):
    with SqlAlchemyUnitOfWork() as uow:
        handler = GetStoreQueryHandler(uow)
        try:
            return handler.handle(GetStoreQuery(store_id))
        except NotFoundException as e:
            raise HTTPException(status_code=404, detail=str(e))
        

@router.get("/stores", response_model=list[StoreReadDTO])
def get_all_stores():
    with SqlAlchemyUnitOfWork() as uow:
        handler = GetAllStoresQueryHandler(uow)
        return handler.handle(GetAllStoresQuery())
