from typing import List

from fastapi import APIRouter, HTTPException, status

from src.app.v1.user import schemas
from src.db.session import db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
async def create_new_user(data: schemas.UserCreate):
    for user in db.users.values():
        if user.get("email").lower() == data.email.lower():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Email занят"
            )

    new_user_id = max(db.users.keys(), default=0) + 1
    db.users[new_user_id] = {
        "id": new_user_id,
        "name": data.name,
        "email": data.email,
        "balance": data.balance,
    }

    return db.users[new_user_id]


@router.get("/", response_model=List[schemas.UserOut])
async def get_all_users():
    return db.users.values()
