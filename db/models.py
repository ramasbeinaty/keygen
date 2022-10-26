from db.base import Base
from sqlalchemy import Boolean, Column, Integer, String

class Ambassadors(Base):
    __tablename__ = "ambassadors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    link = Column(String, unique=True, index=True, nullable=True)
    points = Column(Integer, nullable=False, default=0)
    is_valid = Column(Boolean, nullable=False, default=False)