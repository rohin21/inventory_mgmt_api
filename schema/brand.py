from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BrandCreate(BaseModel):

    title: str
    summary: Optional[str] = ""
    content: Optional[str] = ""


class BrandUpdate(BrandCreate):
    id: int
    summary: Optional[str]
    content: Optional[str]


class BrandDelete(BaseModel):
    id: int


class BrandDisplay(BrandCreate):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
