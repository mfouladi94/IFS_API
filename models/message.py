from pydantic import BaseModel
from datetime import datetime


class MessageBase(BaseModel):
    role: str
    content: str


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    id: str
    created_at: datetime
    interaction_id: str

    class Config:
        orm_mode = True
