from pydantic import BaseModel
from typing import Optional


class CategoryCreate(BaseModel):

    parent_id: Optional[int] = None
    title: str
    meta_title: Optional[str] = None
    slug: str
    content: Optional[str] = None


class CategoryUpdate(CategoryCreate):
    id: int


class CategoryDelete(BaseModel):
    id: int


class CategoryDisplay(CategoryCreate):
    id: int
