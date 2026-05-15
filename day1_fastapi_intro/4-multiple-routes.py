from fastapi import FastAPI

app = FastAPI(
    title = "Nikhil's FastApi Server",
    description = "For managing students backend data",
    version = "1.1"
)

# Fake database
students_db = [
    {"id": 1, "name": "Nikhil", "age": 21, "city": "Kadi"},
    {"id": 2, "name": "Rahul",  "age": 22, "city": "Surat"},
    {"id": 3, "name": "Priya",  "age": 20, "city": "Ahmedabad"}
]


@app.get("/")
def root() :
    return {"message" : "backend server is running"}
    
    
@app.get("/students")
def get_students() :
    return students_db
    

@app.get("/students/{id}")
def get_student_by_id(id : int) :
    for student in students_db :
        if student["id"] == id :
            return student
            
    return "Student Not Found"
    
    
@app.get("/students/search/{city}")
def search_by_city(city : str) :
    result = [s for s in students_db if s["city"].lower() == city.lower()]
    
    return {"city" : city, "student" : result, "count" : len(result)}