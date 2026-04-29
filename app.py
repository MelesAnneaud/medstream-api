from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

# Root route
@app.get("/")
def root():
    return {"message": "MedStream API is running 🚀"}

# Hello route
@app.get("/hello")
def hello():
    return {"message": "Hello World"}

# User route
@app.get("/user")
def user():
    return {"name": "Meles", "role": "Backend Developer"}

# Resume route (ONLY ONE)
@app.get("/resume")
def get_resume():
    return FileResponse("Meles_Anneaud_Resume.pdf")
