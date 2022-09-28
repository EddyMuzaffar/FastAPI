from uuid import uuid4
from fastapi import FastAPI
from typing import List
import json

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
        "description": description,
        "price": price,
        "stock": stock
    }
    data['products'].append(new_product)
    with open('db.json', 'w') as f:
        json.dump(data, f, indent=4)
    return data

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
    return product



@app.get("/products/{product_id}")
# read data from db.json by product_id
def read_product(product_id: int):
    for product in data['products']:
        if product['id'] == product_id:
            return product

