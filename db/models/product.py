from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from ..conn import Base
from sqlalchemy import BIGINT, VARCHAR, TEXT, SMALLINT, DATETIME, Column


class Product(Base):
    __tablename__ = 'product'

    id = Column(BIGINT, nullable=False, primary_key=True)
    title = Column(VARCHAR, nullable=False)
    summary = Column(TEXT, nullable=True)
    type = Column(SMALLINT, nullable=False, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(DATETIME, nullable=True, default=None)
    content = Column(TEXT, nullable=True, default=None)
