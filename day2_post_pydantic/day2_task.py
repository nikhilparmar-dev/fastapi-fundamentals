""" 
Complete Product Store API:
Test steps:
- POST 4 different products from /docs
- GET all products
- GET one product by id
- GET /products/stats
- Try POSTing invalid data — see 422 error
"""

from fastapi import FastAPI 
from pydantic import BaseModel, Field 
from typing import Optional
from fastapi.responses import JSONResponse

app = FastAPI()

products_db = []
counter = 1

class Product(BaseModel) :
    name : str = Field(min_length=2)
    price : float = Field(gt=0)
    quantity : int = Field(ge=0)
    city : str 
    in_stock : bool = True
    discription : Optional[str] = None


# Endpoints:
# 1. GET  /products  → all products → ?city=Kadi to filter
@app.get("/products") 
def get_products(city : Optional[str] = None) :
    if city :
        filtered = [p for p in products_db if city.lower() == p["city"].lower()]
        return filtered 
        
    return products_db



"""
2. GET  /products/stats    → return:
    → total products
    → total in_stock
    → most expensive product name
    → cheapest product name """
@app.get("/products/stats") 
def get_stats() :
    in_stock = 0
    expensive_cost = 0
    cheapest_cost = 0
    expensive = ""
    cheapest = ""

    for product in products_db :
        if product["in_stock"] :
            in_stock += 1
            
    for product in products_db :
        if product["price"] > expensive_cost:
            expensive_cost = product["price"]
            expensive = product["name"]
            
    for product in products_db :
        if product["price"] < cheapest_cost:
            cheapest_cost = product["price"]
            cheapest = product["name"]

    return {
        "Total Products" : len(products_db),
        "Total In Stock" : in_stock,
        "Most Expensive Product" : expensive,
        "Cheapest Product" : cheapest
    }
    
    
    
# 3. GET  /products/{id}  → one product  → 404 if not found
@app.get("/products/{id}")
def get_product(id : int) :
    for product in products_db :
        if product["id"] == id :
            return product 
            
    return JSONResponse(status_code=404, content={"message" : "not found"})



# 4. POST /products   → create new product   → return 201 + created data
@app.post("/products") 
def create_product (product: Product) :
    global counter 
    new = product.dict()
    new["id"] = counter 
    products_db.append(new)
    counter += 1
    
    return JSONResponse(status_code=201, content={"message" : "created", "data" : new})


