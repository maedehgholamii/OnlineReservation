from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base
from model.tools.validator import *

class Reserve(Base):
    __tablename__ = "reserve_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)


    _timing_id = Column("timing_id", Integer, ForeignKey("timing_tbl.id"))
    timing = relationship("Timing")

    _customer_id = Column("customer_id", Integer, ForeignKey("customer_tbl.id"))
    customer = relationship("Customer")