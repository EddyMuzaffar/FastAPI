from fastapi import FastAPI

from data import pingAllTeam,get_full_Name,pingSelectedTeam;
import User

from datetime import datetime


app = FastAPI()


from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123

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
