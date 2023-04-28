
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
class Builds:
    def __init__(self, Premises: Optional[List[Premise]] = None, Apartments: Optional[List[Apartment]] = None, Houses: Optional[List[House]] = None):
        self.Premises = Premises
        self.Apartments = Apartments
        self.Houses = Houses

class Input1:
    def __init__(self, services: Dict[str, bool], builds: Builds):
        self.services = services
        self.builds = builds

class Input2:
    def __init__(self, budget: float, typeBuilder: str, requiredServices: List[str], commercialActivity: Optional[str] = None, wannaPetFriendly: Optional[bool] = None, minDanger: Optional[str] = None):
        self.budget = budget
        self.typeBuilder = typeBuilder
        self.requiredServices = requiredServices
        self.commercialActivity = commercialActivity
        self.wannaPetFriendly = wannaPetFriendly
        self.minDanger = minDanger
        
       

