import json
from fastapi import FastAPI
from pydantic import BaseModel


class Lieux(BaseModel):
    id: int
    name: str
    location: str


app = FastAPI()

with open('db.json', 'r') as f:
    people = json.load(f)


@app.get("/lieux/")
def get_lieux():
    return people


@app.post("/lieux/")
def post_lieu(lieu: Lieux):
    with open('db.json', mode="w") as f:
        people['lieux'].append(lieu.dict())
        f.write(json.dumps(people))
    return people



