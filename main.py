import json
from typing import List

from fastapi import FastAPI, Query

f = open('db.json', 'r')
data = json.load(f)

app = FastAPI()


@app.get("/")
# read all data from db.json
def read_root():
    return data


# --------------------------------------- Product --------------------------------------- #
# add new product to db.json
@app.post("/products/add")
def add_product(name: str, description: str, price: float, stock: int):
    last_product_id = data['products'][-1]['id']
    new_product = {
        "id": last_product_id + 1,
        "name": name,
        "description": description if description else None,
        "price": price,
        "stock": stock
    }
    data['products'].append(new_product)
    with open('db.json', 'w') as f:
        json.dump(data, f, indent=4)
    return data['products']


# update product by product_id
@app.put("/products/update/{product_id}")
def update_product(product_id: int, name: str, description: str, price: float, stock: int):
    for product in data['products']:
        if product['id'] == product_id:
            product['name'] = name
            product['description'] = description
            product['price'] = price
            product['stock'] = stock
    with open('db.json', 'w') as f:
        json.dump(data, f, indent=4)
    return data['products']


# delete product by product_id
@app.delete("/products/delete/{product_id}")
def delete_product(product_id: int):
    for product in data['products']:
        if product['id'] == product_id:
            data['products'].remove(product)
    with open('db.json', 'w') as f:
        json.dump(data, f, indent=4)
    return data['products']


@app.get("/products/{product_id}")
# read data from db.json by product_id
def read_product(product_id: int):
    for product in data['products']:
        if product['id'] == product_id:
            return product


# -------------------------------------- People -------------------------------------- #
# add new people to db.json
@app.post("/people/add")
def add_people(people_id: int, name: str, age: int, gender: str, tools: List[str] = Query(None)):
    last_people_id = data['people'][-1]['id']
    new_people = {
        "id": last_people_id + 1,
        "people_id": people_id,
        "name": name,
        "age": age,
        "gender": gender,
        "tools": tools
    }
    data['people'].append(new_people)
    with open('db.json', 'w') as f:
        json.dump(data, f, indent=4)
    return data['people']


@app.get("/people/{people_id}")
# read data from db.json by people_id
def read_people(people_id: int):
    for people in data['people']:
        if people['id'] == people_id:
            return people


@app.get("/people")
# read all people from db.json
def read_all_people():
    return data['people']


# update people by people_id
@app.put("/people/update/{people_id}")
def update_people(people_id: int, name: str, age: int, gender: str, tools: List[str] = Query(None)):
    for people in data['people']:
        if people['id'] == people_id:
            people['name'] = name
            people['age'] = age
            people['gender'] = gender
            people['tools'] = tools
    with open('db.json', 'w') as f:
        json.dump(data, f, indent=4)
    return data['people']


# delete people by people_id
@app.delete("/people/delete/{people_id}")
def delete_people(people_id: int):
    for people in data['people']:
        if people['id'] == people_id:
            data['people'].remove(people)
    with open('db.json', 'w') as f:
        json.dump(data, f, indent=4)
    return data['people']


# --------------------------------------- Order --------------------------------------- #
# add new order to db.json
@app.post("/orders/add")
def add_order(products: List[int], people_id: int):
    last_order_id = data['orders'][-1]['id']
    # calculate total price from all products in this order
    total_price = 0
    for product_id in products:
        for product in data['products']:
            if product['id'] == product_id:
                total_price += product['price']

    new_order = {
        "id": last_order_id + 1,
        "products": products,
        "people_id": people_id,
        "total_price": total_price

    }

    data['orders'].append(new_order)
    with open('db.json', 'w') as f:
        json.dump(data, f, indent=4)
    return data['orders']
