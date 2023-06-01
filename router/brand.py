from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from db import get_db
from typing import List
from schema import BrandDisplay, BrandCreate, BrandUpdate
from models import Brand

router = APIRouter(tags=['brand'], prefix="/brand")


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[BrandDisplay])
def get_brands(db: Session = Depends(get_db)):
    result = db.query(Brand).all()
    print(result)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Brands available")
    return result


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BrandDisplay)
def create_brand(brand_info: BrandCreate, db: Session = Depends(get_db)):
    brand = Brand(**brand_info.dict())
    db.add(brand)
    db.commit()
    db.refresh(brand)
    if brand is None:
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED, detail="Brand not created")
    return brand


@router.get("/{id}", status_code=status.HTTP_302_FOUND, response_model=BrandDisplay)
def get_brand(id: int, db: Session = Depends(get_db)):
    brand = db.query(Brand).filter(Brand.id == id).first()
    if brand is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Brand not found")
    return brand


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=BrandDisplay)
def update_brand(id: int, brand_update: BrandUpdate, db: Session = Depends(get_db)):
    brands = db.query(Brand).filter(Brand.id == id)
    brand = brands.first()
    if brand is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Brand not found")
    brands.update(brand_update.dict(), synchronize_session = False)
    db.commit()
    return brands.first()


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_brand(id: int, db: Session = Depends(get_db)):
    brands = db.query(Brand).filter(Brand.id == id)
    brand = brands.first()
    if brand is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Brand not found")
    brands.delete(synchronize_session = False)
    db.commit()