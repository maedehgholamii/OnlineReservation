from model.da.da import DataAccess
from view.component.label_text import TextWithLabel
from view.component.table import Table
from model.entity import *
import tkinter as tk
import tkinter.messagebox as msg
from tkinter import ttk

class OnlineReservationView:
    def beauty_job_table_click(self, row):
        print(row)

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

        self.win = tk.Tk()
        self.win.title("Login")
        self.win.geometry("500x500")

        self.username = TextWithLabel(self.win, "username", x=20, y=20)
        self.password = TextWithLabel(self.win, "password", x=20, y=50)
        tk.Button(self.win, text='vorod', command=self.check, bg="lightblue").place(x=60, y=80)

        self.beauty_job_table = Table(self.win,
                                      ["Id", "Title", "Image", "Description"],
                                      [60, 80, 80, 80, 50], 20, 120,  # Adjusted y position
                                      self.beauty_job_table_click)
        self.beauty_job_table.refresh_table(self.beauty_job_da.find_all())

        self.customer_table = Table(self.win,
                                    ["Id", "Name", "Family", "Mobile", "Instagram_Id", "Telegram_id"],
                                    [60, 80, 80, 80, 50, 60, 60], 300, 120,  # Adjusted y position
                                    self.customer_table_click)
        self.customer_table.refresh_table(self.customer_da.find_all())

        self.employee_table = Table(self.win, ["Id", "Name", "Family", "Mobile", "Instagram Id", "Telegram_id"],
                                    [60, 80, 80, 80, 50, 60, 60], 20, 250,  # Adjusted y position
                                    self.employee_table_click)
        self.employee_table.refresh_table(self.employee_da.find_all())

        self.timing_table = Table(self.win, ["Shift Date", "Start Time", "End Time"],
                                  [60, 80, 80], 300, 250,  # Adjusted y position
                                  self.timing_table_click)
        self.timing_table.refresh_table(self.timing_da.find_all())

        self.reserve_table = Table(self.win, ["Shift Date", "Start Time", "End Time"],
                                   [60, 80, 80], 20, 380,  # Adjusted y position
                                   self.reserve_table_click)
        self.reserve_table.refresh_table(self.reserve_da.find_all())

        self.total = TextWithLabel(self.win, "total", 400, 450)

    def check(self):
        username = self.username.get_text()
        password = self.password.get_text()

        print(f"Username: {username}, Password: {password}")



