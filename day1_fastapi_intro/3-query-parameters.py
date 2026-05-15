from fastapi import FastAPI

app = FastAPI()

@app.get("/search")
def search_student(city : str, limit : int = 10) :
    return {
        "Searching_City" : city,
        "limit" : limit,
        "message" : f"Searching {limit} students from {city}"
    }