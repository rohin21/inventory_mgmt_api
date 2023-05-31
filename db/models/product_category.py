from ..conn import Base
from sqlalchemy import BIGINT, Column, ForeignKey


class ProductCategory(Base):
    __tablename__ = "product_category"

    product_id = Column(BIGINT, ForeignKey("product.id"), nullable=False)
    category_id = Column(BIGINT, ForeignKey("category.id"), nullable=False)
