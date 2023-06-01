from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from db import get_db
from typing import List
from schema import CategoryCreate, CategoryUpdate, CategoryDisplay
from models import Category

router = APIRouter(tags=['Category'], prefix="/category")


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[CategoryDisplay])
def get_all(db: Session = Depends(get_db)):
    result = db.query(Category).all()
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categories not available")
    return result


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CategoryDisplay)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    new_category = Category(**category.dict())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    if new_category is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Category not created")
    return new_category


@router.get("/{id}", status_code=status.HTTP_302_FOUND, response_model=CategoryDisplay)
def get_by_id(id: int, db: Session = Depends(get_db)):
    query_result = db.query(Category).filter(Category.id == id).first()
    if query_result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Requested resource not found")
    return query_result
