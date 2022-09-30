import json

from fastapi import FastAPI, HTTPException

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Optional

from starlette import status

app = FastAPI()


class Product(BaseModel):
    id_product = int
    name: str
    description: Optional[str] = None
    price: float
    stock: int


class Tools(BaseModel):
    id_tool: int
    name_tool: str


class Person(BaseModel):
    id_person: int
    name: str
    age: int
    gender: Optional[str] = None
    tools: Optional[Tools] = []


class Order(BaseModel):
    id_order: int
    products: Optional[Product] = []
    id_product: Optional[int] = None
    id_person: Optional[Person] = []
    price = float


with open('people.json', 'r') as f:
    people = json.load(f)['people']

with open('people.json', 'r') as f:
    orders = json.load(f)['orders']

with open('people.json', 'r') as f:
    products = json.load(f)['products']


# ----------------- PEOPLE ----------------- #
@app.get('/people')
def get_person():
    return people


@app.get('/people/{id_person}', status_code=status.HTTP_200_OK)
def get_person(p_id: int):
    person = [p for p in people if p['id_person'] == p_id]
    return person[0] if len(person) > 0 else {}


@app.post('/people', status_code=status.HTTP_201_CREATED)
def post_person(person: Person):
    """

    :param person:
    :return:
    """
    person_data = jsonable_encoder(person)
    for person in people:
        if person['id_person'] == person_data['id_person']:
            res = {
                "success": False,
                "msg": 'Person already have this ID'
            }
            return res
    people.append(person_data)
    write_json()
    res = {
        "success": True,
        "data": person_data,
        "msg": 'Person has been post'

    }
    return res


@app.delete("/people/{id_person}", status_code=status.HTTP_200_OK)
def delete_person(id_person: int):
    """

    :param id_person:
    :return:
    """
    for person in people:
        if person['id_person'] == id_person:
            people.remove(person)
            res = {
                "success": True,
                "data": person

            }
            return res
    raise HTTPException(status_code=403, detail="People not found")


@app.get('/people/{id_person}/tools', status_code=status.HTTP_200_OK,)
def get_tools_person(id_person: int):
    """

    :param id_person:
    :return:
    """
    for person in people:
        if person['id_person'] == id_person:
            if len(person['tools']):
                res = person['tools']
                return res
            else:
                raise HTTPException(status_code=404, detail="Tools not found")
    raise HTTPException(status_code=404, detail="People not found")


@app.get('/people/', status_code=status.HTTP_200_OK)
def get_person_by_tools_name(tool_name: str):
    """

    :param tool_name:
    :return:
    """
    people_match = []
    for p in people:
        for tool in p['tools']:
            if tool_name == tool['name_tool']:
                people_match.append(p)
    return people_match


@app.post('/people/{id_person}/tools', status_code=status.HTTP_201_CREATED)
def post_tools_person(id_person: int, tool: Tools):
    """

    :param id_person:
    :param tool:
    :return:
    """
    json_tools_data = jsonable_encoder(tool)
    for person in people:
        if person['id_person'] == id_person:
            person['tools'].append(json_tools_data)
            write_json()
            res = {
                "success": True,
                "data": person['tools']
            }
            return res
    raise HTTPException(status_code=404, detail="People not found")


@app.get('/people/{id_person}/order', status_code=status.HTTP_200_OK)
def get_tools_person(id_person: int):
    """

    :param id_person:
    :return:
    """
    orders_match = []
    for order in orders:
        if id_person == order['id_person']:
            orders_match.append(order)
    if len(orders_match) > 0:
        res = {
            "success": True,
            "data": orders_match
            }
        return res
    else:
        raise HTTPException(status_code=404, detail="Not order found")







def write_json():
    json = {
        "people": people,
        "orders": orders,
        "products": products,

    }
    json_dat = json.dumps(json)
    json_file = open("people.json", "w")
    json_file.write(json_dat)
    json_file.close()
