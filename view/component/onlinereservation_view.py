from model.da.da import DataAccess
from view.component.label_text import TextWithLabel
from view.component.table import Table
from model.entity.beauty_job import BeautyJob
from model.entity.customer import Customer
from model.entity.employee import Employee
from model.entity.reserve import Reserve
from model.entity.timing import Timing
from tkinter import *
import re
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk

class OnlineReservationView:
    # def beauty_job_table_click(self,row):
    #     print (row)
    #
    # def customer_table_click(self, row):
    #     print(row)
    #
    # def employee_table_click(self, row):
    #     print(row)
    #
    # def reserve_table_click(self, row):
    #     print(row)
    #
    # def timing_table_click(self, row):
    #     print(row)

    def __init__(self):
        self.beauty_job_da = DataAccess(BeautyJob)
        self.customer_da = DataAccess(Customer)
        self.employee_da = DataAccess(Employee)
        self.timing_da = DataAccess(Timing)
        self.reserve_da = DataAccess(Reserve)
        self.win = Tk()
        self.win.title("title")
        self.win.geometry("500x500")
        self.username = TextWithLabel(self.win,"username",x = 20 , y = 80)
        self.password = TextWithLabel(self.win,"password",x = 20 , y = 100)
        Button(self.win,text='vorod',command=self.check).place(x=20,y=140)
        # self.beauty_job_table = Table(self.win,
        #                      ["Id", "Title", "Image", "Description"],
        #                      [60,80,80,80,50], 20, 20 ,
        #                      self.beauty_job_table_click)
        #
        # self.beauty_job_table.refresh_table(self.beauty_job_da.find_all())
        # self.customer_table = Table(self.win,
        #                      ["Id","Name","Family","Mobile", "Instagram_Id", "Telegram_id"],
        #                      [60,80,80,80,50,60,60],300,20 ,
        #                      self.customer_table_click)
        #
        #
        #
        # user_list = [("maedeh", "maedeh"), ("navid", "navid")]
        #
        # def login():
        #     if (username.get(), password.get()) in user_list:
        #         msg.showinfo("Login", "Welcome")
        #
        #     else:
        #         msg.showerror("Access Denied", "Invalid Username or Password")


        #
        # # Id
        # Label(win, text="Username").place(x=20, y=20)
        # username = StringVar()
        # username_txt = Entry(win, textvariable=username)
        # username_txt.place(x=100, y=20)
        #
        # # Name
        # Label(win, text="Password").place(x=20, y=70)
        # password = StringVar()
        # password_txt = Entry(win, textvariable=password)
        # password_txt.place(x=100, y=70)
        #
        # Button(win, text="Login", width=10, command=login).place(x=60, y=170)

        self.win.mainloop()

    def check(self):
        print(self.username.text,self.password.text)
ui = OnlineReservationView()