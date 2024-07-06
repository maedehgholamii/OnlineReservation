from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base
from model.tools.validator import *

class Customer(Base):
    __tablename__ = "customer_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(20))
    _family = Column("family", String(20))
    _mobile = Column("mobile", String(11))
    _instagram_id = Column("instagram_id", String(20))
    _telegram_id = Column("telegram_id", String(30))