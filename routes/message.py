from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models.message import MessageCreate, Message
from models.interaction import Interaction
from db import InteractionModel, MessageModel

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/interactions/{interaction_id}/messages/", response_model=Message)
async def create_message(interaction_id: str, message: MessageCreate, db: Session = Depends(get_db)):
    interaction_db = db.query(InteractionModel).filter(InteractionModel.id == interaction_id).first()
    if not interaction_db:
        raise HTTPException(status_code=404, detail="Interaction not found")

    message_db = MessageModel(**message.dict(), interaction_id=interaction_id)
    db.add(message_db)
    db.commit()
    db.refresh(message_db)
    return message_db


@router.get("/interactions/{interaction_id}/messages/", response_model=List[Message])
async def get_all_messages(interaction_id: str, db: Session = Depends(get_db)):
    messages_db = db.query(MessageModel).filter(MessageModel.interaction_id == interaction_id).all()
    return messages_db
