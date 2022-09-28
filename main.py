import json

from fastapi import FastAPI
from enum import Enum

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Optional
app = FastAPI()


class Person(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    gender: str
    tools: dict


with open('people.json', 'r') as f:
    people = json.load(f)['people']


@app.get('/si/{p_id}')
def get_person(p_id: int):
    person = [p for p in people if p['id'] == p_id]
    return person[0] if len(person) > 0 else {}


@app.post('/people')
def post_person(person: Person):
    json_people_data = jsonable_encoder(person)
    people.append(json_people_data)
    jsonr = {
        "people": people
    }
    json_dat = json.dumps(jsonr)
    json_file = open("people.json", "w")
    json_file.write(json_dat)
    json_file.close()
    return people


@app.delete("/si/{id}")
def destroy_person(id: int):
    for person in people:
        if person['id'] == id:
            people.remove(person)
            jsonr = {
                "people": people
            }
            json_dat = json.dumps(jsonr)
            json_file = open("people.json", "w")
            json_file.write(json_dat)
            json_file.close()
            return "Product Deleted"
    return "product Not Found"


@app.get('/people/{id_person}/tools')
def post_person(id_person):
    person = [p for p in people if p['id'] == id_person]
    return person[0]['tools'] if len(person) > 0 else {}



