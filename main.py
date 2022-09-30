import json

from fastapi import FastAPI

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Optional

from starlette import status

app = FastAPI()




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
    id_product: list
    id_person: int


with open('people.json', 'r') as f:
    people = json.load(f)['people']

with open('people.json', 'r') as f:
    orders = json.load(f)['orders']


@app.get('/people')
def get_person():
    return people


@app.get('/people/{id_person}')
def get_person(p_id: int):
    person = [p for p in people if p['id_person'] == p_id]
    return person[0] if len(person) > 0 else {}


@app.post('/people', status_code=status.HTTP_201_CREATED)
def post_person(person: Person):
    person_data = jsonable_encoder(person)
    for person in people:
        if person['id_person'] == person_data['id_person']:
            res = {
                "success": False,
                "msg" : 'Person already have this ID'
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


@app.delete("/people/{id_person}", status_code=status.HTTP_200_OK )
def delete_person(id_person: int):
    for person in people:
        if person['id_person'] == id_person:
            people.remove(person)
            res = {
                "success": True,
                "data": person['tools']

            }
            return res
    res = {
        "success": False,
        "msg": "No ID for this person"

    }
    return res


@app.get('/people/{id_person}/tools', status_code=status.HTTP_200_OK)
def get_tools_person(id_person: int):
    for person in people:
        if person['id_person'] == id_person:
            if 'tools' in person:
                res = {
                    "success": True,
                    "data": person['tools']

                }
                return res
            else:
                res = {
                    "success": False,
                    "msg": 'No tools for this person'
                }
                return res
    res = {
        "success": False,
        "msg": "No people match"
    }
    return res


@app.get('/people/', status_code=status.HTTP_200_OK)
def get_person_by_tools_name(tool_name: str):
    people_match = []
    for p in people:
        for tool in p['tools']:
            if tool_name == tool['name_tool']:
                people_match.append(p)
    return people_match


@app.post('/people/{id_person}/tools', status_code=status.HTTP_201_CREATED)
def post_tools_person(id_person: int, tool: Tools):
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
    res = {
        "success": False,
        "msg": "No people match"
    }
    return res


@app.get('/people/{id_person}/order', status_code=status.HTTP_200_OK)
def get_tools_person(id_person: int):
    orders_match = []
    for oder in orders:
        if id_person == oder['id_person']:
            orders_match.append(oder)
    if len(orders_match) > 0:
        res = {
            "success": True,
            "data": orders_match
            }

    else:
        res = {
            "success": False,
            "msg": "No people match"
        }
    return res







def write_json():
    jsonr = {
        "people": people,
        "orders": orders
    }
    json_dat = json.dumps(jsonr)
    json_file = open("people.json", "w")
    json_file.write(json_dat)
    json_file.close()
