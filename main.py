from uuid import uuid4
from fastapi import FastAPI, Query
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


# -------------------------------------- Clients -------------------------------------- #
# add new client to db.json
@app.post("/clients/add")
def add_client(email: str, firstname: str, lastname: str, orders: List[int] = Query(None)):
    last_client_id = data['clients'][-1]['id']
    new_client = {
        "id": last_client_id + 1,
        "email": email,
        "firstname": firstname,
        "lastname": lastname,
        "orders": orders
    }
    data['clients'].append(new_client)
    with open('db.json', 'w') as f:
        json.dump(data, f, indent=4)
    return data['clients']


# --------------------------------------- Order --------------------------------------- #
# add new order to db.json with multiple products, each product has quantity, and total price, and client_id
@app.post("/orders/add")
def add_order(products: List[int], client_id: int):
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
        "client_id": client_id,
        "total_price": total_price

    }
    
    data['orders'].append(new_order)
    with open('db.json', 'w') as f:
        json.dump(data, f, indent=4)
    return data['orders']
