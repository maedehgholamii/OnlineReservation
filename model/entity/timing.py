from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date,Time
from sqlalchemy.orm import relationship
from model.entity.base import Base
from model.tools.validator import *

class Timing(Base):
    __tablename__ = "timing_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _shift_date = Column("shift_date",Date)
    _start_time = Column("start_time",Time)
    _end_time = Column("end_time", Time)

    _employee_id = Column("employee_id", Integer, ForeignKey("employee_tbl.id"))
    employee = relationship("Employee")

    _beauty_job_id = Column("beauty_job_id", Integer, ForeignKey("beauty_job_tbl.id"))
    beauty_job = relationship("BeautyJob")
