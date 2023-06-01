from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ProductCreate(BaseModel):
    title: str
    summary: Optional[str]
    type: int
    content: Optional[str]


class ProductUpdate(ProductCreate):
    id: int


class ProductDelete(BaseModel):
    id: int


class ProductDisplay(ProductCreate):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
