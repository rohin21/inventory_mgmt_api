from sqlalchemy import Integer, String, Column, DATETIME, ForeignKey, TEXT
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from ..conn import Base

class ProductMeta(Base):
    __tablename__ = 'product_meta'

    id = Column(Integer, nullable=False, primary_key=True)
    product_id = Column(Integer, ForeignKey("product.id", ondelete="CASCADE"), nullable=False)
    key = Column(String, nullable=False)
    content = Column(TEXT, nullable=True, default=None)
