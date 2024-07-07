from controller.exceptions.exceptions import CustomerNotFoundError
from model.da.da import *
from model.entity.customer import Customer

class CustomerService:

    @staticmethod
    def save(customer):
        customer_da = DataAccess(Customer)
        customer_da.save(customer)
        return customer
    @staticmethod
    def edit(customer):
        customer_da = DataAccess(Customer )
        if customer_da.find_by_id(customer.id):
            customer_da.edit(customer)
            return customer
        else:
            raise CustomerNotFoundError()
    @staticmethod
    def remove(id):
        customer_da = DataAccess(Customer)
        if customer_da.find_by_id(id):
            return customer_da.remove(id)
        else:
            raise CustomerNotFoundError()

    @staticmethod
    def find_all():
        customer_da = DataAccess(Customer)
        return customer_da.find_all()

    @staticmethod
    def find_by_id(id):
        customer_da = DataAccess(Customer)
        return customer_da.find_by_id(id)