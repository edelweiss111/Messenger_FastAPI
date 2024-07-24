from fastapi import APIRouter
from models.user import User

router = APIRouter()

user_db = []


@router.post('/users/', response_model=User)
async def register_user(user: User):
    user_db.append(user)
    return user
