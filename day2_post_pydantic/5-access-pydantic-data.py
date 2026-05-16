from fastapi import FastAPI 
from pydantic import BaseModel 

app = FastAPI()

class Product(BaseModel) :
    name : str
    price : int
    quantity : int
    
    
@app.post("/products")
def create_product(product : Product) :
    print(product.name)
    print(product.price)
    
    new_dict = product.dict()
    
    new_dict["id"] = 1
    new_dict["in_stock"] = True
    
    return new_dict