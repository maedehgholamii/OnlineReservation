from model.entity.reserve import Reserve
from model.service.reserve_service import ReserveService
from model.tools.decorators import exception_handling
from model.tools.logger import Logger

class ReserveController:
    @classmethod
    @exception_handling
    def save(cls, shift_date, start_time, end_time):
        reserve = Reserve(shift_date, start_time, end_time)
        ReserveService.save(reserve)
        return True, reserve

    @classmethod
    @exception_handling
    def edit(cls,id,shift_date, start_time, end_time):
        reserve = Reserve(shift_date, start_time, end_time)
        reserve.id = id
        ReserveService.edit()
        return True, reserve