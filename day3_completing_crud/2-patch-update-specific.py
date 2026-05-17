from fastapi import FastAPI 
from pydantic import BaseModel
from typing import Optional 
from fastapi.responses import JSONResponse

app = FastAPI()

students_db = [
    {"id": 1, "name": "Nikhil", "age": 21, "city": "Kadi"},
    {"id": 2, "name": "Rahul",  "age": 22, "city": "Surat"}
]

class Student(BaseModel) :
    name : Optional[str] = None
    age : Optional[int] = None
    city : Optional[str] = None
    
    
@app.patch("/students/{student_id}")
def patch_partial(student_id : int, student : Student) :
    for patch_student in students_db :
        if patch_student["id"] == student_id :
            if student.name is not None :
                patch_student["name"] = student.name
            if student.age is not None :
                patch_student["age"] = student.age
            if student.city is not None :
                patch_student["city"] = student.city
            return {"message" : "Updated", "Data" : patch_student}
            
    return JSONResponse(
        status_code=404,
        content={"error" : "Not Found"})