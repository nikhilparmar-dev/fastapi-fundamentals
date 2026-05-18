from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

products_db = []
counter = 1


class Product(BaseModel):
    name: str = Field(min_length=2)
    price: float = Field(gt=0)
    city: str


class UpdateProduct(BaseModel):
    name: Optional[str] = Field(default=None, min_length=2)
    price: Optional[float] = Field(default=None, gt=0)
    city: Optional[str] = None


# Create Product
@router.post("/", status_code=201)
def create_product(product: Product):
    global counter

    new_product = product.model_dump()
    new_product["id"] = counter

    products_db.append(new_product)
    counter += 1

    return {
        "message": "Product Created",
        "data": new_product
    }


# Get All Products
@router.get("/")
def get_all_products():
    return {
        "total_products": len(products_db),
        "products": products_db
    }


# Get Single Product
@router.get("/{id}")
def get_single_product(id: int):
    for product in products_db:
        if product["id"] == id:
            return {
                "data": product
            }

    raise HTTPException(
        status_code=404,
        detail="Product Not Found"
    )


# Update Full Product
@router.put("/{id}")
def update_product(id: int, update: Product):
    for product in products_db:
        if product["id"] == id:

            product["name"] = update.name
            product["price"] = update.price
            product["city"] = update.city

            return {
                "message": "Product Updated",
                "data": product
            }

    raise HTTPException(
        status_code=404,
        detail="Product Not Found"
    )


# Update Partial Product
@router.patch("/{id}")
def update_partial_product(id: int, update: UpdateProduct):
    for product in products_db:
        if product["id"] == id:

            if update.name is not None:
                product["name"] = update.name

            if update.price is not None:
                product["price"] = update.price

            if update.city is not None:
                product["city"] = update.city

            return {
                "message": "Product Partially Updated",
                "data": product
            }

    raise HTTPException(
        status_code=404,
        detail="Product Not Found"
    )


# Delete Product
@router.delete("/{id}")
def delete_product(id: int):
    for product in products_db:
        if product["id"] == id:

            products_db.remove(product)

            return {
                "message": "Product Deleted",
                "data": product
            }

    raise HTTPException(
        status_code=404,
        detail="Product Not Found"
    )