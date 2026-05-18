from fastapi import APIRouter
from pydantic import BaseModel, Field 

router = APIRouter(
            prefix="/products",
            tags=["Products"]
        )
       
         
products_db = []
counter = 1


class Product(BaseModel) :
    name : str = Field(min_length=2)
    price: float = Field(gt=0)
    city: str


# Create Product 
@router.post("/")
def create_product(product : Product) :
    global counter 
    new =  product.dict()
    new["id"] = counter
    products_db.append(new)
    
    return {
        "message" : "Product Created",
        "Data" : new
    }
    
    

# get all Products 
@router.get("/")
def get_products() :
    
    return {
        "Total Products" : len(products_db),
        "Products" : products_db
    }