from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from db.conn import Base
from sqlalchemy import BIGINT, VARCHAR, TEXT, SMALLINT, Column


class Product(Base):
    __tablename__ = 'product'

    id = Column(BIGINT, nullable=False, primary_key=True)
    title = Column(VARCHAR, nullable=False)
    summary = Column(TEXT, nullable=True)
    type = Column(SMALLINT, nullable=False, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP, nullable=True, default=None)
    content = Column(TEXT, nullable=True, default=None)
