from fastapi import FastAPI 
from routers import students, products

app = FastAPI(
            Title="Nikhil's API Server",
            Description="Api for students and Products data management",
            Version="1.1"
       )
       
       
# Register Routers
app.include_router(students.router)
app.include_router(products.router)


# Creating Root
@app.get("/")
def root() :
    return {
        "message" : "API SERVER IS RUNNING",
        "Docs" : "/docs"
    }