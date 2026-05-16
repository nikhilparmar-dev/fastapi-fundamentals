from typing import Optional
from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel) :
    name : str
    age : int
    city : str
    course : str
    GitHub : Optional[str] = None
    skills : list = []
    
    
@app.post("/students/create")
def create_student(student : Student) :
    return student
    
    