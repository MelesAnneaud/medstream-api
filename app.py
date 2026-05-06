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

from fastapi import FastAPI

app = FastAPI()

users = [
    {"id": 1, "name": "Meles", "role": "Junior Backend Developer"},
    {"id": 2, "name": "John", "role": "IT Support"}
]

@app.get("/")
def home():
    return {"message": "Backend API is running"}

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}

@app.post("/users")
def create_user(id: int, name: str, role: str):
    new_user = {"id": id, "name": name, "role": role}
    users.append(new_user)
    return {"message": "User created", "user": new_user}

@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, role: str):
    for user in users:
        if user["id"] == user_id:
            user["name"] = name
            user["role"] = role
            return {"message": "User updated", "user": user}
    return {"error": "User not found"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return {"message": "User deleted"}
    return {"error": "User not found"}
