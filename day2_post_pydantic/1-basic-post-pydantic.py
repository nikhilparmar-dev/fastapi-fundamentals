from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel) :
    name : str
    age : int
    city : str
    course : str
  

@app.post("/students")
def add_student(student : Student) :
    return {
        "message" : "Student added Successfully",
        "Student Data" : student
    }
