from sqlalchemy import Integer, String, Column, DATETIME
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from ..conn import Base


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, nullable=False, primary_key=True)
    title = Column(String, nullable=False)
    summary = Column(String, nullable=True)
    type = Column(Integer, nullable=False, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(DATETIME, nullable=True, default=None)
    content = Column(String, nullable=True, default=None)
