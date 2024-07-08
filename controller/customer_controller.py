from model.entity.customer import Customer
from model.service.customer_service import CustomerService
from model.tools.decorators import exception_handling
from model.tools.logger import Logger

class CustomerController:
    @classmethod
    @exception_handling
    def save(cls, name, family,mobile,instagram_id, telegram_id):
        customer = Customer(name,family,mobile,instagram_id,telegram_id)
        CustomerService.save(customer)
        return True, customer

    @staticmethod
    @exception_handling
    def edit(cls,id,name,family,mobile,instagram_id,telegram_id):
        customer = Customer(name,family,mobile,instagram_id,telegram_id)
        customer.id = id
        CustomerService.edit(customer)
        return True, customer

    @staticmethod
    def remove(cls,id):
        customer = CustomerService.remove(id)
        Logger.info(f"Customer Removed - {customer}")
        return True, customer

    @staticmethod
    @exception_handling
    def find_all(cls,):
        customer_list = CustomerService.find_all()
        Logger.info(f"Customer FindAll()")
        return True, customer_list

    @staticmethod
    @exception_handling
    def find_by_id(cls,id):
        customer = CustomerService.find_by_id(id)
        Logger.info(f"Customer Find By Id({id})")
        return True, customer

    @staticmethod
    @exception_handling
    def find_by_name(cls,name):
        customer = CustomerService.find_by_name(name)
        Logger.info(f"Customer Find By Name({name})")
        return True, customer

    @staticmethod
    @exception_handling
    def find_by_mobile(cls,mobile):
        customer = CustomerService.find_by_mobile(mobile)
        Logger.info(f"Customer Find By Mobile({mobile})")
        return True, customer

#todo : dg che find by hayi dashte basham???