from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, Time
from sqlalchemy.orm import relationship
from model.entity.base import Base
from model.tools.validator import *


class Reserve(Base):
    __tablename__ = "reserve_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _shift_date = Column("shift_date", Date)
    _start_time = Column("start_time", Time)
    _end_time = Column("end_time", Time)

    def __init__(self, id, shift_date, start_time, end_time):
        self._id = None
        self._shift_date = shift_date
        self._start_time = start_time
        self._end_time = end_time


    _timing_id = Column("timing_id", Integer, ForeignKey("timing_tbl.id"))
    timing = relationship("Timing")

    _customer_id = Column("customer_id", Integer, ForeignKey("customer_tbl.id"))
    customer = relationship("Customer")

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def shift_date(self):
        return self._shift_date

    @shift_date.setter
    def shift_date(self, shift_date):
        self._shift_date = shift_date

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        self._start_time = start_time

    @property
    def timing_id(self):
        return self._timing_id

    @timing_id.setter
    def timing_id(self, timing_id):
        self._timing_id = timing_id
