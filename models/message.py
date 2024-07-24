from pydantic import BaseModel, EmailStr
from datetime import datetime


class Message(BaseModel):
    sender: str
    receiver: str
    content: str
    timestamp: datetime = datetime.now()
