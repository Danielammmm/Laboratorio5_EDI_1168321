
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
with open("C:\\Users\\danie\\onedrive\\ED!\\LABED_2\\lab2_ED\\input_challenge2.jsonl") as f:
    for r in range(100):
        json_object = f.readline().strip()
        input_lab = json.loads(json_object)
        pricee = [0.0] * 1000
        determinar_vacio = [False, False, False]
        color_d = 0
        res = 0
        idr = [""] * 1000

        if input_lab["input2"]["typeBuilder"] == "Apartments":
            for item in input_lab["input1"]:
                if item["builds"]["Apartments"] is not None:
                    pfs = [a["isPetFriendly"] for a in item["builds"]["Apartments"]]
                    budgets = [a["price"] for a in item["builds"]["Apartments"]]

                    for i in range(len(item["builds"]["Apartments"])):
                        if pfs[i] == input_lab["input2"]["wannaPetFriendly"] and budgets[i] <= input_lab["input2"]["budget"]:
                            idr[res] = item["builds"]["Apartments"][i]["id"]
                            pricee[res] = budgets[i]
                            res += 1
        elif input_lab["input2"]["typeBuilder"] == "Houses":
            for item in input_lab["input1"]:
                if item["builds"]["Houses"] is None:
                    continue

                determinar_vacio[1] = True
                id_ = [house["id"] for house in item["builds"]["Houses"]]
                precio = [house["price"] for house in item["builds"]["Houses"]]
                color = [0] * len(item["builds"]["Houses"])

                for j in range(len(item["builds"]["Houses"])):
                    house = item["builds"]["Houses"][j]
                    id_[j] = house["id"]
                    precio[j] = house["price"]

                    # Asignar el número dependiendo del color de zona de riesgo.
                    if house["zoneDangerous"] == "Green":
                        color[j] = 3
                    elif house["zoneDangerous"] == "Yellow":
                        color[j] = 2
                    elif house["zoneDangerous"] == "Orange":
                        color[j] = 1
                    elif house["zoneDangerous"] == "Red":
                        color[j] = 0
                        if input.input2.typeBuilder == "Houses":
for i in range(len(input.input1)):
if input.input1[i].builds.Houses == None:
continue 
        DeterminarVacio[1] = True
        id = []
        precio = []
        Color = []

        for j in range(len(input.input1[i].builds.Houses)):
            house = input.input1[i].builds.Houses[j]
            id.append(house.id)
            precio.append(house.price)

            # Asignar el número dependiendo del color de zona de riesgo.
            if house.zoneDangerous == "Green":
                Color.append(3)
            elif house.zoneDangerous == "Yellow":
                Color.append(2)
            elif house.zoneDangerous == "Orange":
                Color.append(1)
            elif house.zoneDangerous == "Red":
                Color.append(0)

        DeterminarVacio[1] = False

        for j in range(len(input.input1[i].builds.Houses)):
            if Color[j] <= ColorD and precio[j] <= input.input2.budget:
                idr[res] = id[j]
                pricee[res] = precio[j]
                res += 1

elif input.input2.typeBuilder == "Premises":
    totalPremises = 0
    for i in input.input1:
        if i.builds.Premises != None:
            totalPremises += len(i.builds.Premises)

    idr = [""] * totalPremises
    pricee = [0.0] * totalPremises
    res = 0
    index = 0

    for i in input.input1:
        if i.builds.Premises != None:
            for p in i.builds.Premises:
                if input.input2.commercialActivity in p.commercialActivities and p.price <= input.input2.budget:
                    idr[index] = p.id
                    pricee[index] = p.price
                    index += 1
                    res += 1

# Ordenar valores usando quicksort
def Quicksort(arr, ids, left, right):
    if left < right:
        pivotIndex = Partition(arr, ids, left, right)
        Quicksort(arr, ids, left, pivotIndex - 1)
        Quicksort(arr, ids, pivotIndex + 1, right)

def Partition(arr, ids, left, right):
    pivotValue = arr[right]
    pivotIndex = left - 1
    for i in range(left, right):
        if arr[i] <= pivotValue:
            pivotIndex += 1
            arr[i], arr[pivotIndex] = arr[pivotIndex], arr[i]
            ids[i], ids[pivotIndex] = ids[pivotIndex], ids[i]
    arr[pivotIndex + 1], arr[right] = arr[right], arr[pivotIndex + 1]
    ids[pivotIndex + 1], ids[right] = ids[right], ids[pivotIndex + 1]
    return pivotIndex + 1

# Llamar a Quicksort para ordenar los arreglos
Quicksort(pricee, idr, 0, res - 1)

respuestaFinal = "["
for i in range(res):
    respuestaFinal += f'"{idr[i]}"'
    if i < res - 1:
        respuestaFinal += ","
respuestaFinal += "]"

print(respuestaFinal)
