
from model.entity import *



class Timing(Base):
    __tablename__ = "timing_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _shift_date = Column("shift_date", Date)
    _start_time = Column("start_time", Time)
    _end_time = Column("end_time", Time)

    def __init__(self,shift_date, start_time,end_time):
        self._id = None
        self._shift_date = shift_date
        self._start_time = start_time
        self._end_time = end_time

    employee_id = Column("employee_id", Integer, ForeignKey("employee_tbl.id"))
    employee = relationship("Employee")

    #_beauty_job_id = Column("beauty_job_id", Integer, ForeignKey("beauty_job_tbl.id"))
    #beauty_job = relationship("BeautyJob")

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
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        self._end_time = end_time
