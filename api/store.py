import asyncio
from fastapi import APIRouter, Depends, HTTPException
from application.store.build_store import build_store
from application.store.queries.get_store import GetAllStoresQuery, GetAllStoresQueryHandler, GetStoreQuery, GetStoreQueryHandler
from infraestructure.unit_of_work import SqlAlchemyUnitOfWork
from application.store.commands.create_store import CreateStoreCommand, CreateStoreHandler
from application.store.dto import StoreCreateDTO, StoreReadDTO, StoreReadWithDeliveryTimeDTO
from utils.exceptions import NotFoundException
from application.store.dto_builder import StoreReadDTOBuilder

router = APIRouter()

@router.post("/stores", response_model=StoreReadDTO)
def create_store(data: StoreCreateDTO):
    with SqlAlchemyUnitOfWork() as uow:
        handler = CreateStoreHandler(uow)
        return handler.handle(CreateStoreCommand(data))



@router.get("/stores/{store_id}", response_model=StoreReadWithDeliveryTimeDTO)
async def get_store(store_id: int):
    with SqlAlchemyUnitOfWork() as uow:
        handler = GetStoreQueryHandler(uow)
        try:
            store= handler.handle(GetStoreQuery(store_id))
            builder = StoreReadDTOBuilder(store).calculate_delivery_time()
            await builder.calculate_services()
            await builder.calculate_store_evaluation()
            return builder.build()
        except NotFoundException as e:
            raise HTTPException(status_code=404, detail=str(e))
        

@router.get("/stores", response_model=list[StoreReadDTO])
def get_all_stores():
    with SqlAlchemyUnitOfWork() as uow:
        handler = GetAllStoresQueryHandler(uow)
        return handler.handle(GetAllStoresQuery())
    

@router.get("/storesWithData", response_model=list[StoreReadWithDeliveryTimeDTO])
async def get_all_stores_with_delivery_time():
    with SqlAlchemyUnitOfWork() as uow:
        handler = GetAllStoresQueryHandler(uow)
        stores = handler.handle(GetAllStoresQuery())            
        # Ejecuta todos los builds en paralelo
        result = await asyncio.gather(*(build_store(store) for store in stores))
        return result