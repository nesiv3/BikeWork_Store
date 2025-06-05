from dataclasses import dataclass

@dataclass
class Store:
    id: int
    name: str
    address: str
    document_type: str
    document_number: str
    phone_number: str