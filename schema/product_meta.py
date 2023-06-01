from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ProductMetaCreate(BaseModel):
    product_id: int
    key: str
    content: Optional[str] = None


class ProductMetaUpdate(ProductMetaCreate):
    id: int


class ProductMetaDelete(BaseModel):
    id: int


class ProductMetaDisplay(ProductMetaCreate):
    id: int
