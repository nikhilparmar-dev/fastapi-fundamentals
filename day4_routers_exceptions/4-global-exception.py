from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(Exception)
def global_exception_handler(request : Request, exc : Exception) :
    return JSONResponse(
        status_code=404,
        content={
            "error" : "Internal Server Error",
            "message" : str(exc)
        }
    )
    
    
@app.exception_handler(404)
def not_found_handle(request : Request, exc) :
    return JSONResponse(
        status_code=505,
        content={
            "error" : "Routs not found"
        }
    )