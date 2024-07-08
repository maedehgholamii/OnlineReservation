from model.entity.timing import Timing
from model.service.timing_service import TimingService
from model.tools.decorators import exception_handling
from model.tools.logger import Logger

class TimingController:
    @classmethod
    @exception_handling
    def save(cls,shift_date, start_time,end_time):
        timing = Timing(shift_date, start_time,end_time)
        TimingService.save(timing)
        return True, timing

    @classmethod
    @exception_handling
    def edit(cls,id,shift_date, start_time,end_time):
        timing = Timing(shift_date, start_time,end_time)
        timing.id = id
        TimingService.edit(timing)
        return True, timing

    @classmethod
    def remove(cls,id):
        timing = TimingService.remove(id)
        Logger.info(f"Timing Removed - {timing}")
        return True, timing

    @classmethod
    @exception_handling
    def find_all(cls,):
        timing_list = TimingService.find_all()
        Logger.info(f"Timing FindAll()")
        return True, timing_list

    @classmethod
    @exception_handling
    def find_by_id(cls,id):
        timing = TimingService.find_by_id(id)
        Logger.info(f"Timing Find By Id({id})")
        return True, timing
