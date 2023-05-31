from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from ..conn import Base
from sqlalchemy import BIGINT, VARCHAR, FLOAT, SMALLINT, DATETIME, ForeignKey, Column


class Item(Base):
    __tablename__ = 'item'

    id = Column(BIGINT, nullable=False, primary_key=True)
    product_id = Column(BIGINT, ForeignKey("product.id"), nullable=False)
    brand_id = Column(BIGINT, ForeignKey("brand.id"), nullable=False)
    supplier_id = Column(BIGINT, ForeignKey("user.id"), nullable=False)
    order_id = Column(BIGINT, ForeignKey("order.id"), nullable=False)
    sku = Column(VARCHAR, nullable=False)
    mrp = Column(FLOAT, nullable=False, default=0)
    discount = Column(FLOAT, nullable=False, default=0)
    price = Column(FLOAT, nullable=False, default=0)
    quantity = Column(SMALLINT, nullable=False, default=0)
    sold = Column(SMALLINT, nullable=False, default=0)
    available = Column(SMALLINT, nullable=False, default=0)
    defective = Column(SMALLINT, nullable=False, default=0)
    created_by = Column(BIGINT, nullable=False)
    updated_by = Column(BIGINT, default=None)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(DATETIME, nullable=True, default=None)
