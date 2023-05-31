from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from db.conn import Base
from sqlalchemy import BIGINT, SMALLINT, FLOAT, VARCHAR, TEXT, Column, ForeignKey


class Order(Base):
    __tablename__ = 'order'

    id = Column(BIGINT, nullable=False, primary_key=True)
    user_id = Column(BIGINT, ForeignKey("user.id"), nullable=False, index=True)
    type = Column(SMALLINT, nullable=False, default=0)
    status = Column(SMALLINT, nullable=False, default=0)
    sub_total = Column(FLOAT, nullable=False, default=0)
    item_discount = Column(FLOAT, nullable=False, default=0)
    tax = Column(FLOAT, nullable=False, default=0)
    shipping = Column(FLOAT, nullable=False, default=0)
    total = Column(FLOAT, nullable=False, default=0)
    promo = Column(VARCHAR, nullable=True, default=None)
    discount = Column(FLOAT, nullable=False, default=0)
    grand_total = Column(FLOAT, nullable=False, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP, nullable=True, default=None)
    content = Column(TEXT, nullable=True, default=None)
