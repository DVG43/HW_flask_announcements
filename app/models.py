from sqlalchemy.orm import declarative_base
from sqlalchemy import (
      Column,
      Integer,
      DateTime,
      String,
      func,
)

Base = declarative_base()

class Announsment(Base):

    __tablename__ = 'announsments'
    id = Column(Integer, primary_key=True)
    headline = Column(String(100), index=True, nullable=False)
    description = Column(String(200), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    owner = Column(String(50), nullable=False)