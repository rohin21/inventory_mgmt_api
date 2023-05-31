from db.conn import Base
from sqlalchemy import BIGINT, VARCHAR, TEXT, ForeignKey, Column


class Category(Base):
    __tablename__ = "category"

    id = Column(BIGINT, nullable=False, primary_key=True)
    parent_id = Column(BIGINT, ForeignKey("category.id"), nullable=True)
    title = Column(VARCHAR, nullable=False)
    meta_title = Column(VARCHAR, nullable=True, default=None)
    slug = Column(VARCHAR, nullable=False)
    content = Column(TEXT, nullable=True, default=None)
