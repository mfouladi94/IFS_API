from fastapi import FastAPI
from routes import interaction, message
from db import engine, Base
import os
from dotenv import load_dotenv


load_dotenv()

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(interaction.router, prefix="/api/v1")
app.include_router(message.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
