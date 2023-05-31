from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from db.conn import Base
from sqlalchemy import BIGINT, VARCHAR, Column, ForeignKey


class Address(Base):
    __tablename__ = 'address'

    id = Column(BIGINT, nullable=False, primary_key=True)
    user_id = Column(BIGINT, ForeignKey("user.id"), nullable=True, default=None, index=True)
    order_id = Column(BIGINT, ForeignKey("order.id"), nullable=True, default=None, index=True)
    first_name = Column(VARCHAR, nullable=True, default=None)
    middle_name = Column(VARCHAR, nullable=True, default=None)
    last_name = Column(VARCHAR, nullable=False, default=None)
    mobile = Column(VARCHAR, nullable=True)
    email = Column(VARCHAR, nullable=True)
    line_1 = Column(VARCHAR, nullable=True, default=None)
    line_2 = Column(VARCHAR, nullable=True, default=None)
    city = Column(VARCHAR, nullable=True, default=None)
    province = Column(VARCHAR, nullable=True, default=None)
    country = Column(VARCHAR, nullable=True, default=None)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP, nullable=True, default=None)
