from datetime import datetime

from databases import Database
from sqlalchemy import create_engine, Column, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
database = Database(DATABASE_URL)
Base = declarative_base()


class InteractionModel(Base):
    __tablename__ = "interactions"

    id = Column(String, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    model_name = Column(String)
    role = Column(String)
    prompt = Column(String)


class MessageModel(Base):
    __tablename__ = "messages"

    id = Column(String, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    role = Column(String)
    content = Column(String)
    interaction_id = Column(String, ForeignKey('interactions.id'))


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
