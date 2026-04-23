from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "MedStream API is running 🚀"}

@app.get("/hello")
def hello():
    return {"message": "Hello World"}

@app.get("/user")
def user():
    return {"name": "Meles", "role": "Backend Developer"}

@app.post("/data")
def receive_data(data: dict):
    return {"received": data}

@app.get("/resume")
def get_resume():
    return FileResponse(
        "Meles_Anneaud_Resume.pdf",
        media_type="application/pdf",
        filename="Meles_Anneaud_Resume.pdf"
    )
