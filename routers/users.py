from fastapi import APIRouter
from schemas.user import User
from crud.users import get_user_by_email, create_user
from fastapi import HTTPException


router = APIRouter()


@router.post('/users/')
async def register_user(user: User):
    check_user = await get_user_by_email(user.email)
    if check_user:
        raise HTTPException(status_code=400, detail="Пользователь с таким email уже существует")
    new_user = await create_user(user.name, user.email)
    return {"user_id": new_user}
