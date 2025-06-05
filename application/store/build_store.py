import asyncio
from application.store.dto_builder import StoreReadDTOBuilder


async def build_store(store):
    builder = StoreReadDTOBuilder(store).calculate_delivery_time()
    await asyncio.gather(
        builder.calculate_services(),
        builder.calculate_store_evaluation()
    )
    return builder.build()