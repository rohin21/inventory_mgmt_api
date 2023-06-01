from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class OrderCreate(BaseModel):

    user_id: int
    type: int
    status: int
    sub_total: float
    item_discount: float
    tax: float
    shipping: float
    total: float
    promo: Optional[str]
    discount: float
    grand_total: float
    created_at: datetime
    updated_at: Optional[datetime] = None
    content: Optional[str]


class OrderUpdate(OrderCreate):

    id: int


class OrderDelete(BaseModel):

    id: int


class OrderDisplay(OrderCreate):

    id: int