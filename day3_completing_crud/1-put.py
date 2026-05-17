from fastapi import FastAPI 
from pydantic import BaseModel 
from fastapi.responses import JSONResponse 

app = FastAPI()

students_db = [
    {"id": 1, "name": "Nikhil", "age": 21, "city": "Kadi"},
    {"id": 2, "name": "Rahul",  "age": 22, "city": "Surat"}
]


class Student(BaseModel) :
    id : int
    name : str
    age : int
    city : str


@app.put("/students/{student_id}")
def update_student(student_id : int, student : Student) :
    for db_student in students_db :
        if db_student["id"] == student_id :
            db_student["id"] = student_id
            db_student["name"] = student.name
            db_student["age"] = student.age
            db_student["city"] = student.city
            
            return {"message" : "Updated",
            "Data" : db_student}
            
    return JSONResponse(status_code=404, content={"message" : "student not found"})
