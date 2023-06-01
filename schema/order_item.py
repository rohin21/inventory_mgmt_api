from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class OrderItemCreate(BaseModel):

    product_id: int
    item_id: int
    order_id: int
    sku: str
    price: float
    discount: float
    quantity: int
    content: Optional[str]


class OrderItemUpdate(OrderItemCreate):

    id: int


class OrderItemDelete(BaseModel):

    id: int


class OrderItemDisplay(OrderItemCreate):

    id: int
    created_at: datetime
    updated_at: Optional[datetime]