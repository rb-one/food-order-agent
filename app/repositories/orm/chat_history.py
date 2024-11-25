from datetime import datetime, timezone

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import MappedColumn, mapped_column

from app.repositories.orm import Base


class ChatHistory(Base):
    __tablename__ = "chat_history"

    id: MappedColumn[int] = mapped_column(Integer, primary_key=True, index=True)
    session_id: MappedColumn[str] = mapped_column(String, index=True)
    user_message: MappedColumn[str] = mapped_column(String)
    ai_message: MappedColumn[str] = mapped_column(String)
    created_atM: MappedColumn[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )

    def __repr__(self):
        return f"<ChatHistory(session_id={self.session_id}, created_at={self.created_at})>"
