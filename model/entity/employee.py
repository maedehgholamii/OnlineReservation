from model.entity import *



class Employee(Base):
    __tablename__ = "employee_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(20))
    _family = Column("family", String(20))
    _mobile = Column("mobile", String(11))
    _instagram_id = Column("instagram_id", String(20))
    _telegram_id = Column("telegram_id", String(30))

    def __init__(self, name, family, mobile, instagram_id, telegram_id):
        self._id = None
        self._name = name
        self._family = family
        self._mobile = mobile
        self._instagram_id = instagram_id
        self._telegram_id = telegram_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name_validator(name,"Invalid Name!!")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = name_validator(family,"Invalid Family!!")

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        self._mobile = mobile_validator(mobile,"Invalid Mobile!!")

    @property
    def instagram_id(self):
        return self._instagram_id

    @instagram_id.setter
    def instagram_id(self, instagram_id):
        self._instagram_id = instagram_id

    @property
    def telegram_id(self):
        return self._telegram_id

    @telegram_id.setter
    def telegram_id(self, telegram_id):
        self._telegram_id = telegram_id
