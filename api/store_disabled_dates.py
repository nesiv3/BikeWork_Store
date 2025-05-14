from fastapi import APIRouter, Depends, HTTPException



from application.store_disabled_dates.queries.get_store_disabled_dates import (
    GetStoreDisabledDatesQuery, GetStoreDisabledDatesQueryHandler
)
from typing import List
from datetime import date

from infraestructure.unit_of_work import SqlAlchemyUnitOfWork

router = APIRouter()

@router.get("/disabled_dates/{store_id}", response_model=List[date])
async def get_store_disabled_dates(store_id: int):
    with SqlAlchemyUnitOfWork() as uow:
        handler = GetStoreDisabledDatesQueryHandler(uow)
        return await handler.handle(GetStoreDisabledDatesQuery(store_id))