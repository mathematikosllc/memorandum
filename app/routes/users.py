from fastapi import APIRouter
from app.models import database, schemas

router = APIRouter()


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate):
    user_data = {"id": str(schemas.uuid4()), **user.model_dump()}
    database.users_db.append(user_data)
    return user_data
