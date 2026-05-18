from fastapi import FastAPI, HTTPException

db = [{
       "id" : 1,
       "name" : "Nikhil",
       "age" : 17
   }]
   
app = FastAPI()

@app.get("/students/{id}")
def get_student(id : int):
    for student in db :
        if id == student["id"] :
            return student 
            
    raise HTTPException(
    status_code=404,
    detail="Student Not Found"
    )