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
    
@app.delete("/students/{student_id}")
def delete_student(student_id : int, student : Student) : 
    for student in students_db :
        if student_id == student["id"] :
            deleted = students_db.pop(student_id-1)
            return {"message" : "Deleted", "Deleted" : student}
            
    return JSONResponse(status_code=404, content={"error" : "Not Found"})
        