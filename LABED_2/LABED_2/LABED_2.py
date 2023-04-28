
import json
from typing import Dict, List, Optional

class House:
    def __init__(self, zoneDangerous: str, address: str, price: float, contactPhone: str, id: str):
        self.zoneDangerous = zoneDangerous
        self.address = address
        self.price = price
        self.contactPhone = contactPhone
        self.id = id

class Apartment:
    def __init__(self, isPetFriendly: bool, address: str, price: float, contactPhone: str, id: str):
        self.isPetFriendly = isPetFriendly
        self.address = address
        self.price = price
        self.contactPhone = contactPhone
        self.id = id

class Premise:
    def __init__(self, commercialActivities: List[str], address: str, price: float, contactPhone: str, id: str):
        self.commercialActivities = commercialActivities
        self.address = address
        self.price = price
        self.contactPhone = contactPhone
        self.id = id


