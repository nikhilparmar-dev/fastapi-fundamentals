from fastapi import FastAPI 
from pydantic import BaseModel 

app = FastAPI()

class StudentInput(BaseModel):
    name: str
    age: int
    password: str
    
    
class StudentOutput(BaseModel) :
    id : int
    name : str
    age : int
    
    
@app.post("/students", response_model=StudentOutput) 
def create_student(student : StudentInput) :
     new_student = {
         "id" : 1,
         "name" : student.name,
         "age" : student.age
     }
     
     return new_student