from pydantic import BaseModel

class StoreMaintenanceDTO(BaseModel):
    id: int
    store_id: int
    name: str
    cost: float
    time: float

    model_config = {
        "from_attributes": True
    }