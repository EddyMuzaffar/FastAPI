import json

from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
from typing import Optional
app = FastAPI()


class Person(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    gender: str


with open('people.json', 'r') as f:
    people = json.load(f)['people']


@app.get('/si/{p_id}')
def get_person(p_id: int):
    person = [p for p in people if p['id'] == p_id]
    return person[0] if len(person) > 0 else {}


@app.get('/slo')
def slo():
    return {"Some": "Something"}

