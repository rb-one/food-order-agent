from datetime import datetime, timezone

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import MappedColumn, mapped_column

from app.repositories.orm import Base


class User(Base):
    __tablename__ = "users"

    id: MappedColumn[int] = mapped_column(Integer, primary_key=True, index=True)
    username: MappedColumn[str] = mapped_column(String, unique=True, index=True)
    email: MappedColumn[str] = mapped_column(String, unique=True, index=True)
    password_hash: MappedColumn[str] = mapped_column(String)
    created_at: MappedColumn[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"
