from fastapi import FastAPI 
from pydantic import BaseModel 
from typing import Optional 
from fastapi.responses import JSONResponse

app = FastAPI()

student_db = []
id_counter = 1

class Student(BaseModel) :
    name : str
    age : int
    city : str
    course : str
    
    
# get all students
@app.get("/students")
def get_students() :
    return {
        "students" : student_db,
        "Total Student" : len(student_db)
    }
    
    
# Create a new student
@app.post("/students/create_student")
def create_student(student : Student) :
    global id_counter
    
    new_student = {
        "id" : id_counter,
        "name" : student.name,
        "age" : student.age,
        "city" : student.city,
        "course" : student.course
    }
    
    student_db.append(new_student)
    id_counter += 1
    
    return {
        "message" : "student added Successfully",
        "Student Data" : new_student
    }
    
    
@app.get("/students/{id}")
def get_student(id : int) :
    for student in student_db :
        if student["id"] == id :
            return student
    
    return JSONResponse(
        status_code=404,
        content={"message" : "student not found"}
    )
    