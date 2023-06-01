from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TransactionCreate(BaseModel):
    user_id: int
    order_id: int
    code: str
    type: int
    mode: int
    status: int
    content: Optional[str] = None


class TransactionUpdate(TransactionCreate):
    id: int


class TransactionDelete(BaseModel):
    id: int


class TransactionDisplay(TransactionCreate):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
