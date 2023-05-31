from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BrandCreate(BaseModel):

    title: str
    summary: Optional[str] = None
    content: Optional[str] = None


class BrandUpdate(BrandCreate):
    id: int


class BrandDelete(BaseModel):
    id: int


class BrandDisplay(BrandCreate):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
