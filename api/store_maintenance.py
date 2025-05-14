from fastapi import APIRouter
from typing import List
from infraestructure.unit_of_work import SqlAlchemyUnitOfWork
from application.store_maintenance.queries.store_maintenance import (
    GetStoreMaintenanceQuery, GetStoreMaintenanceQueryHandler
)
from application.store_maintenance.dto import StoreMaintenanceDTO

router = APIRouter()

@router.get("/maintenance/{store_id}", response_model=List[StoreMaintenanceDTO])
def get_store_maintenance(store_id: int):
    print("store_id", store_id)
    with SqlAlchemyUnitOfWork() as uow:
        handler = GetStoreMaintenanceQueryHandler(uow)
        return handler.handle(GetStoreMaintenanceQuery(store_id))