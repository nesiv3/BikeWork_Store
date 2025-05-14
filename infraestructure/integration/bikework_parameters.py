import httpx
from typing import Dict, List
from datetime import date

EXTERNAL_API_URL = "https://bikeworkparamapi-eqe3cbd0euhbe8ge.brazilsouth-01.azurewebsites.net/api/disabled_dates"

async def fetch_external_disabled_dates() -> List[Dict]:
    async with httpx.AsyncClient() as client:
        print('Hola')
        response = await client.get(EXTERNAL_API_URL)
        response.raise_for_status()
        data = response.json()
        return data