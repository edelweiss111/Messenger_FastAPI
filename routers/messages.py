from fastapi import APIRouter
from schemas.message import Message
from typing import List
from crud.messages import get_messages_by_id, create_message
from fastapi import HTTPException

router = APIRouter()


@router.post('/send_message/')
async def send_message(message: Message):
    return await create_message(message.sender_id, message.receiver_id, message.content)


@router.get('/messages/{user_id}/', response_model=List[Message])
async def get_messages(user_id: int):
    messages = await get_messages_by_id(user_id)
    if not messages:
        raise HTTPException(status_code=404, detail='Пользователь не найден')
    return messages
