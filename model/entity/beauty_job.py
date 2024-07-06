from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base
from model.tools.validator import *

class BeautyJob(Base):
    __tablename__ = "beauty_job_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _title = Column("title", String(20), nullable=False, unique = True)
    _image = Column("image", String(50))
    _description = Column("description", String(100))
