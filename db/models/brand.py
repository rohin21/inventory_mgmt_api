from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from ..conn import Base
from sqlalchemy import BIGINT, VARCHAR, TEXT, DATETIME, Column


class Brand(Base):
    __tablename__ = 'brand'

    id = Column(BIGINT, nullable=False, primary_key=True)
    title = Column(VARCHAR, nullable=False)
    summary = Column(VARCHAR, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(DATETIME, nullable=True, default=None)
    content = Column(TEXT, nullable=True, default=None)
    