from fastapi import FastAPI

from data import pingAllTeam,get_full_Name,pingSelectedTeam;
import User

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/team")
def write_table():
    return pingAllTeam()

@app.get("/team/allTeam")
def write_specifiquelyElement():
    return pingAllTeam()

@app.get("/team/{name}/{secondname}")
async def say_hello(name: str,secondname: str):
    return {get_full_Name(name,secondname)}
@app.get("/getName/{name}")
def write_specifiquelyElement(name: str):
    return User.get_person_name(name)
