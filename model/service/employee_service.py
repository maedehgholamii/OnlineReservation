from controller.exceptions.exceptions import EmployeeNotFoundError
from model.da.da import *
from model.entity.employee import Employee

class EmployeeService:

    @staticmethod
    def save(employee):
        employee_da = DataAccess(Employee)
        employee_da.save(employee)
        return employee
    @staticmethod
    def edit(employee):
        employee_da = DataAccess(Employee )
        if employee_da.find_by_id(employee.id):
            employee_da.edit(employee)
            return employee
        else:
            raise EmployeeNotFoundError()
    @staticmethod
    def remove(id):
        employee_da = DataAccess(Employee)
        if employee_da.find_by_id(id):
            return employee_da.remove(id)
        else:
            raise EmployeeNotFoundError()

    @staticmethod
    def find_all():
        employee_da = DataAccess(Employee)
        return employee_da.find_all()

    @staticmethod
    def find_by_id(id):
        employee_da = DataAccess(Employee)
        return employee_da.find_by_id(id)

    @staticmethod
    def find_by_name(name):
        employee_da = DataAccess(Employee)
        return employee_da.find_by_name(Employee.name == name)

    @staticmethod
    def find_by_mobile(mobile):
        employee_da = DataAccess(Employee)
        return employee_da.find_by_mobile(Employee.mobile == mobile)

#todo: dg kodom field haro barash find by benevisam?