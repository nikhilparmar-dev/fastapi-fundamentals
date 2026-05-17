"""
Complete Product CRUD API:

Test flow in /docs:
Step 1 → POST 3 products
Step 2 → GET all → verify 3 exist
Step 3 → PUT product 1 → full replace
Step 4 → PATCH product 2 → change price only
Step 5 → DELETE product 3
Step 6 → GET all → verify only 2 remain
Step 7 → GET deleted product → should return 404
"""


from fastapi import FastAPI 
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field 
from typing import Optional 

app = FastAPI()

product_db = []
counter = 1

class ProductCreate(BaseModel) :
    name: str = Field(min_length=2)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)
    city: str
    category: str
    in_stock: bool = True
    
    
class ProductUpdate(BaseModel) :
    # All fields Optional — for PATCH
    name: Optional[str] = Field(default=None, min_length=2)
    price: Optional[float] = Field(default=None, gt=0)
    quantity: Optional[int] = Field(default=None, ge=0)
    city: Optional[str] = None
    category: str = None
    in_stock: Optional[bool] = True

    
    
# Build all 6 endpoints:

# 1. POST   /products          → create (201)
@app.post("/students", status_code=201)
def create_student(product : ProductCreate) :
    global counter 
    
    new_dict = product.dict()
    new_dict["id"] = counter
    product_db.append(new_dict)
    counter += 1
    
    return {"message" : "Created", "Data" : product}
    
    
    
# 2. GET    /products  → all products  → ?category=electronics filter
@app.get("/products/category")
def get_products(category : Optional[str] = None) :
    if category :
        for product in product_db :
            if category.lower() == product["category"].lower() : 
                return {
                    "Products" : product
                }
        
        return JSONResponse(status_code=404, content={"error" : "Product Not found in this category"})
                                         
    return {
        "Total Products" : len(product_db),
        "Products" : product_db
    }
    
    
    
# 3. GET    /products/{id}     → one product (404 if missing)
@app.get("/students/{id}")
def get_product(id : int) :
    for product in product_db : 
        if id == product["id"] :
            return {"product" : product}
    
    return JSONResponse(status_code=404, content={"error" : "Product Not found"})
    
    
    
# 4. PUT    /products/{id}     → full replace (404 if missing)
@app.put("/products/{id}")
def update_product(id : int, product_update : ProductUpdate) :
    for product in product_db : 
    
        if id == product["id"] :
            product["name"] = product_update.name
            product["price"] = product_update.price
            product["quantity"] = product_update.quantity
            product["city"] = product_update.city
            product["category"] = product_update.category
            product["in_stock"] = product_update.in_stock
                
            return {"message" : "Updated", "Data" : product_update} 
            
    return JSONResponse(status_code=404, content={"error" : "Product Not found"})
    
    
    
# 5. PATCH  /products/{id}     → partial update (404 if missing)
@app.patch("/products/{id}")
def partial_update_product(id : int, product_update : ProductUpdate) :
    for product in product_db : 
    
        if id == product["id"] :
            if product["name"] is not None :
                product["name"] = product_update.name
            if product["price"] is not None :
                product["price"] = product_update.price
            if product["quantity"] is not None :
                product["quantity"] = product_update.quantity
            if product["city"] is not None :
                product["city"] = product_update.city
            if product["category"] is not None :
                product["category"] = product_update.category
            if product["in_stock"] is not None :
                product["in_stock"] = product_update.in_stock
                
            return {"message" : "Updated", "Data" : product_update} 
            
    return JSONResponse(status_code=404, content={"error" : "Product Not found"})
    
    
    
# 6. DELETE /products/{id}     → delete (404 if missing)
@app.delete("/students/{id}")
def delete_product(id : int) :
    for product in product_db : 
        if id == product["id"] :
            removed = product_db.pop(id-1)
            return {"message" : "Product Deleted", "Deleted" : removed}
    
    return JSONResponse(status_code=404, content={"error" : "Product Not found"})