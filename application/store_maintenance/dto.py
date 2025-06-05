from pydantic import BaseModel

class StoreMaintenanceDTO(BaseModel):
    id: int
    store_id: int
    name: str
    cost: float
    time: float
    maintenance_description: str | None = None  # si es opcional
    image: str | None = None  # si es opcional

    model_config = {
        "from_attributes": True
    }