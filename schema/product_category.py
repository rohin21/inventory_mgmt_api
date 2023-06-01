from pydantic import BaseModel


class ProductCategoryCreate(BaseModel):
    product_id: int
    category_id: int


class ProductCategoryUpdate(ProductCategoryCreate):
    pass


class ProductCategoryDelete(ProductCategoryCreate):
    pass


class ProductCategoryDisplay(ProductCategoryCreate):
    pass