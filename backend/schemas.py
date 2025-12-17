from pydantic import BaseModel
from datetime import datetime

class ChatMessageCreate(BaseModel):
    session_id: str
    role: str
    content: str
    timestamp: datetime
