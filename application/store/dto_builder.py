import random
import os
from dotenv import load_dotenv

import httpx
from application.store.dto import StoreReadDTO, StoreReadWithDeliveryTimeDTO
from domain.store import Store


load_dotenv()
MAINTENANCE_COUNT_URL =os.getenv("MAINTENANCE_COUNT_URL", "https://bikeworkmaintenanceapi-ajc7efhqh5djeua5.brazilsouth-01.azurewebsites.net/api/v1/maintenance/count/")
STORE_AVERAGE_RATING_URL = os.getenv("STORE_AVERAGE_RATING_URL", "https://bikeworkstoreapi-ajc7efhqh5djeua5.brazilsouth-01.azurewebsites.net/api/v1/stores/")
class StoreReadDTOBuilder:
    def __init__(self, store: Store):
        self.store = store
        self.delivery_time = None
        self.count_services = None
        self.evaluation = None

    def calculate_delivery_time(self):
        # Lógica para calcular el tiempo de entrega
        self.delivery_time = random.randint(10, 120)  
        return self

    async def calculate_services(self):
        url = f"{MAINTENANCE_COUNT_URL}{self.store.id}"
        print(f"Flag 1: {url}")
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                response = await client.get(url)
                response.raise_for_status()
                # Suponiendo que el JSON tiene {"average_rating": valor}
       
                self.count_services = response.json().get("maintenance_count", -1)
        except Exception as e:
            print(f"Error al obtener count: {e}")
            self.count_services = None
        return self
    
    async def calculate_store_evaluation(self):
        url = f"{STORE_AVERAGE_RATING_URL}{self.store.id}/average-rating"
        print(f"Flag 2: {url}")
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                response = await client.get(url)
                response.raise_for_status()
                # Suponiendo que el JSON tiene {"average_rating": valor}
                self.evaluation = response.json().get("average_rating", -1)
        except Exception as e:
            print(f"Error al obtener average_rating: {e}")
            self.evaluation = None
        return self

    def build(self):

        if self.delivery_time is None:
         self.delivery_time = -1
        if self.count_services is None:
         self.count_services =-1
        if self.evaluation is None:
         self.evaluation = -1

        return StoreReadWithDeliveryTimeDTO(
            id=self.store.id,
            name=self.store.name,
            address=self.store.address,
            document_type=self.store.document_type,
            document_number=self.store.document_number,
            phone_number=self.store.phone_number,
            image=self.store.image,
            delivery_time=self.delivery_time,
            count_services=self.count_services,
            evaluation=self.evaluation,
        )