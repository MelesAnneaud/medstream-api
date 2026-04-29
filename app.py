from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path

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

@app.get("/resume")
def get_resume():
    file_path = Path(__file__).parent / "Meles_Anneaud_Resume.pdf"

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail=f"Resume file not found. Looking for: {file_path}"
        )

    return FileResponse(
        path=str(file_path),
        media_type="application/pdf",
        filename="Meles_Anneaud_Resume.pdf"
    )
