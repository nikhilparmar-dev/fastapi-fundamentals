from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "Name" : "Nikhil"},
    {"id": 2, "Name" : "Prem"},
    {"id": 3, "Name" : "Zeeshan"}
]

@app.get("/")
def wc() :
    return "Welcome to Nikhil's API"

@app.get("/students/{student_id}")
def get_student(student_id : int) :
    for student in students :
        if student["id"] == student_id :
            return student
            
    return "Student Not Found!"
    