from model.entity.employee import Employee
from model.service.employee_service import EmployeeService
from model.tools.decorators import exception_handling
from model.tools.logger import Logger

class CustomerController:
    @classmethod
    @exception_handling
    def save(cls, name, family,mobile,instagram_id, telegram_id):
        employee = Employee(name,family,mobile,instagram_id,telegram_id)
        EmployeeService.save(employee)
        return True, employee

    @staticmethod
    @exception_handling
    def edit(cls,id,name,family,mobile,instagram_id,telegram_id):
        employee = Employee(name,family,mobile,instagram_id,telegram_id)
        employee.id = id
        EmployeeService.edit()
        return True,

    @staticmethod
    def remove(cls,id):
        employee = EmployeeService.remove(id)
        Logger.info(f"Employee Removed - {employee}")
        return True, employee

    @staticmethod
    @exception_handling
    def find_all(cls,):
        employee_list = EmployeeService.find_all()
        Logger.info(f"Employee FindAll()")
        return True, employee_list

    @staticmethod
    @exception_handling
    def find_by_id(cls,id):
        employee = EmployeeService.find_by_id(id)
        Logger.info(f"Employee Find By Id({id})")
        return True, employee

    @staticmethod
    @exception_handling
    def find_by_name(cls,name):
        employee = EmployeeService.find_by_name(name)
        Logger.info(f"Employee Find By Name({name})")
        return True, employee

    @staticmethod
    @exception_handling
    def find_by_mobile(cls,mobile):
        employee = EmployeeService.find_by_mobile(mobile)
        Logger.info(f"Employee Find By Mobile({mobile})")
        return True, employee