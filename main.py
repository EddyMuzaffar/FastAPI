import json
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


class Lieux(BaseModel):
    id: int
    name: str
    location: str


app = FastAPI()

with open('db.json', 'r') as f:
    lieux = json.load(f)


@app.get("/lieux/")
def get_lieux():
    return lieux


@app.post("/lieux/")
def post_lieu(lieu: Lieux):
    with open('db.json', mode="w") as f:
        lieux['lieux'].append(lieu.dict())
        f.write(json.dumps(lieux))
    return lieux

@app.put("/lieux/")
def update_lieu(lieu: Lieux):
    update_lieu_encoded = jsonable_encoder(lieu)
    lieux = update_lieu_encoded

    f.write(json.dumps(lieux))

    return update_lieu_encoded

