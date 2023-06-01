from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserDisplay(BaseModel):

    id: int
    role_id: int
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    user_name: str
    mobile: Optional[str]
    email: Optional[EmailStr]
    intro: Optional[str]
    profile: Optional[str]
    registered_at: datetime
    last_login: Optional[datetime] = None


class UserCreate(BaseModel):

    role_id: int
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    user_name: str
    password: str
    mobile: Optional[str]
    email: Optional[EmailStr]
    intro: Optional[str]
    profile: Optional[str]


class UserUpdate(BaseModel):

    id: int
    role_id: int
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    user_name: Optional[str]
    mobile: Optional[str]
    email: Optional[EmailStr]
    intro: Optional[str]
    profile: Optional[str]


class UserDelete(BaseModel):

    id: int

