from sqlalchemy import Column, BIGINT, SMALLINT, VARCHAR, DATETIME, TEXT
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from ..conn import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(BIGINT, primary_key=True, nullable=False)
    role_id = Column(SMALLINT, nullable=False)
    first_name = Column(VARCHAR, nullable=True, default=None)
    middle_name = Column(VARCHAR, nullable=True, default=None)
    last_name = Column(VARCHAR, nullable=True, default=None)
    user_name = Column(VARCHAR, nullable=True, default=None, unique=True)
    mobile = Column(VARCHAR, nullable=True, unique=True)
    email = Column(VARCHAR, nullable=True, unique=True)
    password_hash = Column(VARCHAR, nullable=False)
    registered_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    last_login = Column(DATETIME, nullable=True, default=None)
    intro = Column(TEXT, nullable=True, default=None)
    profile = Column(TEXT, nullable=True, default=None)
