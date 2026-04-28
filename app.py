from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path

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
@app.get("/resume", response_class=FileResponse)
def get_resume():
    file_path = Path(__file__).parent / "Meles_Anneaud_Resume.pdf"

    return FileResponse(
        path=file_path,
        media_type="application/pdf",
        filename="Meles_Anneaud_Resume.pdf"
    )
