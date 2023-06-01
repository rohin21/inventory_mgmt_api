from pydantic import BaseModel
from typing import Optional


class CategoryCreate(BaseModel):

    parent_id: Optional[int]
    title: str
    meta_title: Optional[str]
    slug: str
    content: Optional[str]


class CategoryUpdate(CategoryCreate):
    id: int


class CategoryDelete(BaseModel):
    id: int


class CategoryDisplay(CategoryCreate):
    id: int
