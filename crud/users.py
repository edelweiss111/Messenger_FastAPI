from models.models import User
from config import database
from sqlalchemy import select

from services import get_db


async def create_user(name: str, email: str):
    db = get_db()
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user.id


async def get_user_by_email(email: str):
    query = select(User).where(User.email == email)
    return await database.fetch_one(query)
