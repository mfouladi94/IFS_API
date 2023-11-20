from pydantic import BaseModel
from typing import List
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


class InteractionCreate(BaseModel):
    model_name: str
    role: str
    prompt: str


class Interaction(InteractionCreate):
    id: str
    created_at: datetime
    updated_at: datetime
    messages: List['Message']

