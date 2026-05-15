from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/students/{student_id}")
def get_student(student_id : int) :
    student = {"id" : 1, "Name" : "Nikhil", "City" : "Kadi"}
   
    if student["id"] == student_id :
        return student
            
    return JSONResponse(
        status_code=404,
        content={"Error" : "Student Not Found"}
    )