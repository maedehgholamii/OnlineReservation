from controller.exceptions.exceptions import ReserveNotFoundError
from model.da.da import *
from model.entity.reserve import Reserve

class ReserveService:

    @staticmethod
    def save(reserve):
        reserve_da = DataAccess(Reserve)
        reserve_da.save(reserve)
        return reserve

    @staticmethod
    def edit(reserve):
        reserve_da = DataAccess(Reserve)
        if reserve_da.find_by_id(reserve.id):
            reserve_da.edit(reserve)
            return reserve
        else:
            raise ReserveNotFoundError()

    @staticmethod
    def remove(id):
        reserve_da = DataAccess(Reserve)
        if reserve_da.find_by_id(id):
            return reserve_da.remove(id)
        else:
            raise ReserveNotFoundError()

    @staticmethod
    def find_all():
        reserve_da = DataAccess(Reserve)
        return reserve_da.find_all()

    @staticmethod
    def find_by_id(id):
        reserve_da = DataAccess(Reserve)
        return reserve_da.find_by_id(id)

#todo : find by ???????