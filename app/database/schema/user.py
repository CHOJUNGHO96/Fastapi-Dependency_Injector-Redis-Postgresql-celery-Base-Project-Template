from sqlalchemy import Column, Integer, String, DateTime

from .base import Base


class User(Base):
    __tablename__ = "user_info"

    user_number = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    user_password = Column(String(255), nullable=False)
    user_email = Column(String(255), nullable=False)
    user_name = Column(String(100), nullable=False)
    is_enable = Column(Integer, default=1)
    reg_date = Column(DateTime)
