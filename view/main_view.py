from tkinter import *
from view.customer_view import CustomerView
from view.reserve_view import ReserveView
from view.beauty_job_view import BeautyJobView
from view.employee_view import EmployeeView
from view.timing_view import TimingView


class MainView:
    def show_view_customer(self):
        ui = CustomerView()
        ui.show()

    def show_view_reserve(self):
        ui = ReserveView()
        ui.show()

    def show_view_beauty_job(self):
        ui = BeautyJobView()
        ui.show()

    def show_view_employee(self):
        ui = EmployeeView()
        ui.show()

    def show_view_timing(self):
        ui = TimingView()
        ui.show
    def __init__(self):
        self.win = Tk()
        self.win.title("Main View")
        self.win.geometry("650x900")

        Label(self.win, text="رزرو آنلاین نوبت", width=20, height=1, bg="aqua", font=("Arial", 18)).place(x=190, y=50)

        Button(self.win, text="خدمات ما", width=20, height=3, bg="aqua", command=self.show_view_beauty_job).place(x=120,
                                                                                                            y=100)
        Button(self.win, text="مشاهده زمان های خالی", width=20, height=3, bg="aqua", command=self.show_view_timing).place(x=400,
                                                                                                                y=100)

        Label(self.win, text="اگر حساب کابری ندارید همین الان ثبت نام کنبد", width=37, height=1, bg="light blue", font=("Arial", 18)).place(x=60,
                                                                                                            y=200)
        Button(self.win, text="وارد کردن اطلاعات ", width=15, height=3, bg="light blue", command=self.show_view_customer).place(
            x=100, y=250)
        Button(self.win, text="رزرو", width=15, height=3, bg="light blue", command=self.show_view_reserve).place(
            x=400, y=250)

        Label(self.win, text="برای همکاری با ما همین حالا ثبت نام کتید", width=37, height=1, bg="pink", font=("Arial", 18)).place(x=60, y=350)

        Button(self.win, text=" ثبت نام", width=15, height=3, bg="pink", command=self.show_view_employee).place(x=260,
                                                                                                            y=400)
        self.win.mainloop()