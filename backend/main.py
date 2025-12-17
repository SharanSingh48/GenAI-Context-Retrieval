from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, SessionLocal
from models import ChatMessage
from schemas import ChatMessageCreate
from database import Base

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/chat")
def create_chat_message(
    message: ChatMessageCreate,
    db: Session = Depends(get_db)
):
    chat_message = ChatMessage(
        session_id=message.session_id,
        role=message.role,
        content=message.content,
        timestamp=message.timestamp
    )
    db.add(chat_message)
    db.commit()
    db.refresh(chat_message)

    return {"status": "success", "id": chat_message.id}
