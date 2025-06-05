from typing import List
from datetime import date

from application.store_special_day_policy.queries.get_store_special_day_policy import GetStoreSpecialDayPolicyQuery, GetStoreSpecialDayPolicyQueryHandler
from infraestructure.integration.bikework_parameters import fetch_external_disabled_dates

class GetStoreDisabledDatesQuery:
    def __init__(self, store_id: int):
        self.store_id = store_id
       

class GetStoreDisabledDatesQueryHandler:
    def __init__(self, uow):
        self.uow = uow

    async def handle(self, query: GetStoreDisabledDatesQuery) -> List[date]:
        local_dates = self.uow.store_disabled_dates.get_dates_by_store_id(query.store_id)
        policy_handler = GetStoreSpecialDayPolicyQueryHandler(self.uow)
        policies =  policy_handler.handle(GetStoreSpecialDayPolicyQuery(query.store_id))
        day_types = [policy.day_type for policy in policies]
        external_dates = await fetch_external_disabled_dates() 
        print("day_types:", day_types)
        print([policy["reason"] for policy in external_dates])
        if day_types:
          holidays_dates = [
              date.fromisoformat(item["the_date"])
              for item in external_dates
              if item["reason"] in day_types
            ]
        else:
            holidays_dates = [
              date.fromisoformat(item["the_date"])
              for item in external_dates
            ]
        return sorted(list(set(local_dates) | set(holidays_dates)))