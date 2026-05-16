from fastapi import FastAPI
from pydantic import BaseModel, Field 

app = FastAPI()

class Student(BaseModel) :
    name : str = Field(min_length=2, max_length=10)
    age : int = Field(ge=1, le=100)
    city : str = Field(min_length=2)
    percentage : float = Field(min=0.00, max=100.00)
    

@app.post("/students/create")
def create_student(student : Student) :
    return {
        "message" : "Validated and created",
        "Student" : student
    } 