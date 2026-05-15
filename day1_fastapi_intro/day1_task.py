# Product API:

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


#database
products_db = [
    {"id": 1, "name": "Laptop",   "price": 45000, "city": "Ahmedabad"},
    {"id": 2, "name": "Mouse",    "price": 500,   "city": "Surat"},
    {"id": 3, "name": "Keyboard", "price": 1200,  "city": "Kadi"},
    {"id": 4, "name": "Monitor",  "price": 12000, "city": "Ahmedabad"},
    {"id": 5, "name": "Webcam",   "price": 2000,  "city": "Kadi"},
]


#Build these endpoints:
# 1. GET / → welcome message
@app.get("/")
def root() :
    return {"message" : "Welcome to Nikhil's Products API"}
    
    
    
# 2. GET /products → all products + total count
@app.get("/products")
def get_products() :
    return {
        "Products" : products_db,
        "Total Products" : len(products_db)
    }



# 3. GET /products/{id}    → one product by id → 404 if not found
@app.get("/products/{product_id}")
def get_product_by_id(product_id : int) :
    for product in products_db :
        if product["id"] == product_id :
            return product
    
    return JSONResponse(
        status_code=404,
        content={"Error" : "Product Not found"}
    )



# 4. GET /products/search/city → ?city=Kadi. → returns filtered products
@app.get("/products/search/city")
def search_product_by_city(city : str) :
    product = [product for product in products_db if product ["city"].lower() == city.lower()]
    
    return {
        "Searched_City" : city,
        "Product" : product,
        "Message" : f"Searching {product} from {city}"
    }



# 5. GET /products/search/price→ ?min=1000&max=15000 → returns products in price range
@app.get("/products/search/price")
def search_product_in_price_range(min : int, max : int) :
    product = [product for product in products_db if min <= product["price"] <= max]
    
    return {
        "Minimum Price" : min,
        "Maximum Price" : max,
        "Product" : product,
        "message" : f"Searching Product between price {min} and {max}"
    }