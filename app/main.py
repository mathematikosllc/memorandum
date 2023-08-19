import uvicorn
from fastapi import FastAPI
from app.routes import users, notes

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(notes.router, prefix="/notes", tags=["notes"])


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8080, reload=True)
