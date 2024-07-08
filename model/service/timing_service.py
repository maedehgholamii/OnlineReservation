from controller.exceptions.exceptions import TimingNotFoundError
from model.da.da import *
from model.entity.timing import Timing

class TimingService:

    @staticmethod
    def save(timing):
        timing_da = DataAccess(Timing)
        timing_da.save(timing)
        return timing

    @staticmethod
    def edit(timing):
        timing_da = DataAccess(Timing)
        if timing_da.find_by_id(timing.id):
            timing_da.edit(timing)
            return timing
        else:
            raise TimingNotFoundError()

    @staticmethod
    def remove(id):
        timing_da = DataAccess(Timing)
        if timing_da.find_by_id(id):
            return timing_da.remove(id)
        else:
            raise TimingNotFoundError()

    @staticmethod
    def find_all():
        timing_da = DataAccess(Timing)
        return timing_da.find_all()

    @staticmethod
    def find_by_id(id):
        timing_da = DataAccess(Timing)
        return timing_da.find_by_id(id)

#todo : find by????????