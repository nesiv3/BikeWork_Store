from typing import List
from application.store_special_day_policy.dto import StoreSpecialDayPolicyDTO

class GetStoreSpecialDayPolicyQuery:
    def __init__(self, store_id: int):
        self.store_id = store_id

class GetStoreSpecialDayPolicyQueryHandler:
    def __init__(self, uow):
        self.uow = uow

    def handle(self, query: GetStoreSpecialDayPolicyQuery) -> List[StoreSpecialDayPolicyDTO]:
        policies = self.uow.store_special_day_policy.get_by_store_id(query.store_id)
        return [StoreSpecialDayPolicyDTO.model_validate(p) for p in policies if p.is_operational]