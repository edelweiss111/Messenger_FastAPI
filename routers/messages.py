from fastapi import APIRouter, HTTPException
from models.message import Message
from typing import List

router = APIRouter()

messages_db = []


@router.post('/send_message/', response_model=Message)
async def send_message(message: Message):
    messages_db.append(message)
    return message


@router.get('/messages/{email}/', response_model=List[Message])
async def get_messages(email: str):
    response = [message for message in messages_db if message.receiver == email]
    if not response:
        raise HTTPException(status_code=404, detail='Пользователь не найден')
    return response
