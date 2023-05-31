from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from db.conn import Base
from sqlalchemy import BIGINT, VARCHAR, SMALLINT, TEXT, Column, ForeignKey


class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(BIGINT, nullable=False, primary_key=True)
    user_id = Column(BIGINT, ForeignKey("user.id"), nullable=False, index=True)
    order_id = Column(BIGINT, ForeignKey("order.id"), nullable=False, index=True)
    code = Column(VARCHAR, nullable=False)
    type = Column(SMALLINT, nullable=False, default=0)
    mode = Column(SMALLINT, nullable=False, default=0)
    status = Column(SMALLINT, nullable=False, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP, nullable=True, default=None)
    content = Column(TEXT, nullable=True, default=None)
