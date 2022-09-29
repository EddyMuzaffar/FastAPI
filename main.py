import json

from fastapi import FastAPI


from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Optional
app = FastAPI()


class Person(BaseModel):
    id: int
    name: str
    age: int
    gender: Optional[str] = None
    tools: Optional[dict] = []


class Tools(BaseModel):
    id_tool: int
    name_tool: str


with open('people.json', 'r') as f:
    people = json.load(f)['people']


@app.get('/people')
def get_person():
    return people


@app.get('/people/{p_id}')
def get_person(p_id: int):
    person = [p for p in people if p['id'] == p_id]
    return person[0] if len(person) > 0 else {}


@app.post('/people')
def post_person(person: Person):
    person_data = jsonable_encoder(person)
    for person in people:
        if person['id'] == person_data['id']:
            res = {
                "success": False,
                "msg": 'Id is already selected'

            }
            return res
    people.append(person_data)
    write_json(people)
    res = {
        "success": True,
        "data": person_data

    }
    return res


@app.delete("/people/{id}")
def delete_person(id: int):
    for person in people:
        if person['id'] == id:
            people.remove(person)
            write_json(people)
            res = {
                "success": True,
                "data": person

            }
            return res
    res = {
        "success": False,
        "msg": "No ID for this person"

    }
    return res


@app.get('/people/{id_person}/tools')
def get_tools_person(id_person: int):
    for person in people:
        if person['id'] == id_person:
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


@app.post('/people/{id_person}/tools')
def post_tools_person(id_person: int, tool: Tools):
    json_tools_data = jsonable_encoder(tool)
    for person in people:
        if person['id'] == id_person:
            if 'tools' in person:
                person['tools'].append(json_tools_data)
            else:
                person['tools'] = [json_tools_data]
            write_json(people)
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


def write_json(data: dict):
    jsonr = {
        "people": data
    }
    json_dat = json.dumps(jsonr)
    json_file = open("people.json", "w")
    json_file.write(json_dat)
    json_file.close()



