from models.models import Message

from services import get_db


async def create_message(sender: int, receiver: int, content: str):
    db = get_db()
    message = Message(sender_id=sender, receiver_id=receiver, content=content)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


async def get_messages_by_id(user_id: int):
    db = get_db()
    messages = db.query(Message).filter((Message.sender_id == user_id) | (Message.receiver_id == user_id)).all()
    return messages
