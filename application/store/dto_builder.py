import random
from application.store.dto import StoreReadDTO, StoreReadWithDeliveryTimeDTO
from domain.store import Store

class StoreReadDTOBuilder:
    def __init__(self, store: Store):
        self.store = store
        self.delivery_time = None

    def calculate_delivery_time(self):
        # Lógica para calcular el tiempo de entrega
        self.delivery_time = random.randint(10, 120)    
        return self

    def build(self):

        return StoreReadWithDeliveryTimeDTO(
            id=self.store.id,
            name=self.store.name,
            address=self.store.address,
            document_type=self.store.document_type,
            document_number=self.store.document_number,
            phone_number=self.store.phone_number,
            image=self.store.image,
            delivery_time=self.delivery_time 
        )