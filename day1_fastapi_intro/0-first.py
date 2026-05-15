from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet() :
	return {"Message" : "Hello, I'm Nikhil Parmar"}
