from sqlalchemy import Column, ForeignKey, BIGINT, VARCHAR, TEXT
from ..conn import Base


class ProductMeta(Base):
    __tablename__ = 'product_meta'

    id = Column(BIGINT, nullable=False, primary_key=True)
    product_id = Column(BIGINT, ForeignKey("product.id"), nullable=False)
    key = Column(VARCHAR, nullable=False)
    content = Column(TEXT, nullable=True, default=None)
