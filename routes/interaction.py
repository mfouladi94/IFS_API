from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models.interaction import InteractionCreate, Interaction
from models.message import MessageCreate
from db import InteractionModel

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/interactions/", response_model=Interaction)
async def create_interaction(interaction: InteractionCreate, db: Session = Depends(get_db)):
    interaction_db = InteractionModel(**interaction.dict())
    db.add(interaction_db)
    db.commit()
    db.refresh(interaction_db)
    return interaction_db


@router.get("/interactions/", response_model=List[Interaction])
async def get_all_interactions(db: Session = Depends(get_db)):
    interactions_db = db.query(InteractionModel).all()
    return interactions_db
