from fastapi import FastAPI

app = FastAPI()

@app.get("/students")
def get_students() :
    students = [
        {"Id" : 1, "Name" : "Nikhil", "City" : "Kadi"},
        {"Id" : 2, "Name" : "Prem", "City" : "Ahmedabad"},
        {"Id" : 3, "Name" : "Zeeshan", "City" : "Gandhinagar"}
    ]
    
    return {"Students" : students, "Total Students" : len(students)}
    
@app.get("/students/first")
def get_first_student() :
    return {"Id" : 1, "Name" : "Nikhil", "City" : "Kadi"}