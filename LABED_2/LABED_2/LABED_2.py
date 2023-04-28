
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
        
       class InputLab:
    def __init__(self, input1: List[Input1], input2: Input2):
        self.input1 = input1
        self.input2 = input2
import json

with open(r"C:\Users\usuario\source\repos\lab2_ED\lab2_ED\input_challenge_lab_2.jsonl") as f:
    json_objects = f.read().splitlines()

for r in range(100):
    input_data = json.loads(json_objects[r])
    price = [0] * 1000
    determinar_vacio = [False] * 3
    color_d = 0
    res = 0
    idr = [''] * 1000

    if input_data['input2']['typeBuilder'] == "Apartments":
        for item in input_data['input1']:
            if item['builds']['Apartments'] is not None:
                pfs = [a['isPetFriendly'] for a in item['builds']['Apartments']]
                budgets = [a['price'] for a in item['builds']['Apartments']]
                
                for i in range(len(item['builds']['Apartments'])):
                    if pfs[i] == input_data['input2']['wannaPetFriendly'] and budgets[i] <= input_data['input2']['budget']:
                        idr[res] = item['builds']['Apartments'][i]['id']
                        price[res] = budgets[i]
                        res += 1
import json

