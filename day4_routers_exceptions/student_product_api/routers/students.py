from fastapi import APIRouter
from pydantic import BaseModel, Field 
from fastapi.responses import JSONResponse 
from typing import Optional 

router = APIRouter(
        prefix="/students",
        tags=["Students"]
    )
    
#fake_db
students_db = []
counter = 1

class CreateStudent(BaseModel) :
    name : str = Field(min_length=2)
    age : int = Field(ge=0, le=100)
    city : str
    course : str
    
class UpdateStudent(BaseModel) :
    name : Optional[str] = Field(min_length=2, default=None)
    age : Optional[int] = Field(ge=0, le=100, default=None)
    city : Optional[str] = None
    course : Optional[str] = None
    

# Create New Student    
@router.post("/", status_code=201)
def create_student(student : CreateStudent) :
    global counter 
    new = student.dict()
    new["id"] = counter
    students_db.append(new)
    counter += 1
    return {
        "message" : "Student Created",
        "student" : new
    }
    
    

# get all students 
@router.get("/") 
def get_all_students() : 
    return {
        "Total Students" : len(students_db),
        "Students" : students_db
    }
    
    
    
# get single student by id 
@router.get("/{id}") 
def get_single_students(id : int) : 
    for student in students_db :
        if student["id"] == id :
            return {
             "Student Data" : student
            }
            
    return JSONResponse(
        status_code=404,
        content={
            "error" : "Student Not Found"
        }
    )
    
    
    
# Update Student Data by id 
@router.put("/{id}")
def update_student(id : int, update : CreateStudent) :
    for student in students_db :
        if student["id"] == id :
            student["name"] = update.name
            student["age"] = update.age
            student["city"] = update.city
            student["course"] = update.course
            
            return {
             "Student Updated" : student
            }
            
    return JSONResponse(
        status_code=404,
        content={
            "error" : "Student Not Found"
        }
    )
    
    
    
# Update Partial Student Data by id 
@router.patch("/{id}")
def update_partial_student(id : int, update : UpdateStudent) :
    for student in students_db :
        if student["id"] == id :
            if update.name is not None :
                student["name"] = update.name
                
            if update.age is not None :
                student["age"] = update.age
                
            if update.city is not None :
                student["city"] = update.city
                
            if update.course is not None :
                student["course"] = update.course
            
            return {
             "Student Data Updated" : student
            }
            
    return JSONResponse(
        status_code=404,
        content={
            "error" : "Student Not Found"
        }
    )
    
    
    
# delete single student by id 
@router.delete("/{id}") 
def delete_student(id : int) : 
    for student in students_db :
        if student["id"] == id :
            removed = students_db.remove(student)
            return {
             "Removed Student" : student
            }
            
    return JSONResponse(
        status_code=404,
        content={
            "error" : "Student Not Found"
        }
    )