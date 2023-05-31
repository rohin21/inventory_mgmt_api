from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ItemCreate(BaseModel):

    product_id: int
    brand_id: int
    supplier_id: int
    order_id: int
    sku: str
    mrp: float
    discount: float
    price: float
    quantity: int
    sold: int
    available: int
    defective: int


class ItemUpdate(ItemCreate):

    id: int
    updated_by: int = None


class ItemDelete(BaseModel):

    id: int
