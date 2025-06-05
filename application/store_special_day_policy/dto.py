from pydantic import BaseModel
from datetime import date, datetime

class StoreSpecialDayPolicyDTO(BaseModel):
    id: int
    store_id: int
    day_type: str
    is_operational: bool
    effective_date: date
    end_date: date | None = None
    created_at: datetime | None = None

    model_config = {
     "from_attributes": True
 }