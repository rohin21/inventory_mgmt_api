from sqlalchemy import Integer, String, DATETIME, Column
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from ..conn import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, nullable=False)
    role_id = Column(Integer, nullable=False)
    first_name = Column(String, nullable=True, default=None)
    middle_name = Column(String, nullable=True, default=None)
    last_name = Column(String, nullable=True, default=None)
    user_name = Column(String, nullable=True, default=None, unique=True)
    mobile = Column(Integer, nullable=True, unique=True)
    email = Column(String, nullable=True, unique=True)
    password_hash = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    last_login = Column(DATETIME, nullable=True, default=None)
    intro = Column(String, nullable=True, default=None)
    profile = Column(String, nullable=True, default=None)
