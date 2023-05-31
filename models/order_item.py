from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from db.conn import Base
from sqlalchemy import BIGINT, VARCHAR, FLOAT, SMALLINT, TEXT, ForeignKey, Column


class OrderItem(Base):
    __tablename__ = 'order_item'

    id = Column(BIGINT, nullable=False, primary_key=True)
    product_id = Column(BIGINT, ForeignKey("product.id"), nullable=False)
    item_id = Column(BIGINT, ForeignKey("item.id"), nullable=False)
    order_id = Column(BIGINT, ForeignKey("order.id"), nullable=False)
    sku = Column(VARCHAR, nullable=False)
    price = Column(FLOAT, nullable=False, default=0)
    discount = Column(FLOAT, nullable=False, default=0)
    quantity = Column(SMALLINT, nullable=False, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP, nullable=True, default=None)
    content = Column(TEXT, nullable=True, default=None)
