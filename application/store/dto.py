from pydantic import BaseModel

class StoreCreateDTO(BaseModel):
    name: str
    address: str
    document_type: str
    document_number: str
    phone_number: str
    image: str | None = None  # si es opcional
    email: str | None = None  # si es opcional


    model_config = {
        "from_attributes": True
    }

class StoreReadDTO(StoreCreateDTO):
    id: int
  

class StoreReadWithDeliveryTimeDTO(StoreReadDTO):
    delivery_time: int 
    count_services: int
    evaluation: float
    class Config:
        orm_mode = True
