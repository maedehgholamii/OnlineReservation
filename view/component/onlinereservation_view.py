from model.da.da import DataAccess
from view.component.label_text import TextWithLabel
from view.component.table import Table
from model.entity.beauty_job import BeautyJob
from model.entity.customer import Customer
from model.entity.employee import Employee
from model.entity.reserve import Reserve
from model.entity.timing import Timing
from tkinter import *

class OnlineReservationView:
    def beauty_job_table_click(self,row):
        print (row)

    def customer_table_click(self, row):
        print(row)

    def employee_table_click(self, row):
        print(row)

    def reserve_table_click(self, row):
        print(row)

    def timing_table_click(self, row):
        print(row)

    def __init__(self):
        self.beauty_job_da = DataAccess(BeautyJob)
        self.customer_da = DataAccess(Customer)
        self.employee_da = DataAccess(Employee)
        self.timing_da = DataAccess(Timing)
        self.reserve_da = DataAccess(Reserve)
        self.win = Tk()
        self.title("Online Reservation View")
        self.win.geometry("500x500")

        beauty_job_table = Table(self.win,
                             ["Id", "Title", "Image", "Description"],
                             [60,80,80,80,50], 20, 20 ,
                             self.beauty_job_table_click)

        self.beauty_job_table.refresh_table(self.beauty_job_da.find_all())
        customer_table = Table(self.win,
                             ["Id","Name","Family","Mobile", "Instagram_Id", "Telegram_id"],
                             [60,80,80,80,50,60,60],300,20 ,
                             self.customer_table_click)

        self.win.mainloop()