from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class AddressCreate(BaseModel):

    user_id: Optional[int]
    order_id: Optional[int]
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    mobile: Optional[str]
    email: Optional[EmailStr]
    line_1: Optional[str]
    line_2: Optional[str]
    city: Optional[str]
    province: Optional[str]
    country: Optional[str]


class AddressUpdate(AddressCreate):
    id: int


class AddressDelete(BaseModel):
    id: int


class AddressDisplay(AddressCreate):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
