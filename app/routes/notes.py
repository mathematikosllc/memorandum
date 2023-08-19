from typing import List
from fastapi import APIRouter, HTTPException
from app.models import database, schemas

router = APIRouter()


@router.post("/", response_model=schemas.Note)
def create_note(note: schemas.NoteCreate):
    user_exists = any(user["id"] == note.user_id for user in database.users_db)
    if not user_exists:
        raise HTTPException(status_code=404, detail="User not found")

    new_id = len(database.notes_db) + 1
    note_data = {"id": new_id, **note.model_dump()}
    database.notes_db.append(note_data)
    return note_data


@router.get("/user/{user_id}", response_model=List[schemas.Note])
def get_notes_for_user(user_id: str):
    return [note for note in database.notes_db if note["user_id"] == user_id]
