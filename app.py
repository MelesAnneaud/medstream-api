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
    base_path = Path(__file__).parent

    pdf_files = list(base_path.rglob("*.pdf"))

    if not pdf_files:
        all_files = [str(file) for file in base_path.rglob("*")]
        raise HTTPException(
            status_code=404,
            detail={"message": "No PDF found", "files": all_files}
        )

    file_path = pdf_files[0]

    return FileResponse(
        path=str(file_path),
        media_type="application/pdf",
        filename=file_path.name
    )
