from fastapi import FastAPI 
from pydantic import BaseModel, Field 
from fastapi.responses import JSONResponse
from typing import Optional

app = FastAPI()

products_db = []
counter = 1

class Product(BaseModel) :
    name : str = Field(min_length=2)
    price : float = Field(gt=0)
    city : str
    in_stock : bool = True
    

@app.get("/products")
def get_all(city : Optional[str] = None) :
    if city :
        filtered = [p for p in products_db if city == p["city"]]
        return filtered
        
    return products_db
    
    
@app.get("/products/{product_id}")
def get_product(id : int) :
    for p in products_db :
        if p["id"] == id :
            return p
            
    return JSONResponse(status_code=404, content={"message" : "product not found"})
    
       
@app.post("/products") 
def create(product : Product) :
    global counter
    new = product.dict()
    new["id"] = counter 
    products_db.append(new)
    counter += 1
    
    return JSONResponse(status_code=201, content={"message" : "created", "data" : new})