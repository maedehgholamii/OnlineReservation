from view.beauty_job_view import BeautyJobView
from view.reserve_view import ReserveView
from view.customer_view import CustomerView
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from view.component.label_text import TextWithLabel


class FrontView:

    def show_view_customer(self):
        msg.showinfo("question", "برای ورود به حساب کاربری ابتدا مشخصات خود را وارد کنید ")
        ui = CustomerView()
        ui.show()

    def show_view_reserve(self):
        ui = ReserveView()
        ui.show()

    def show_view_beauty_job(self):
        ui = BeautyJobView()
        ui.show()

    def show(self):
        self.win = Tk()
        self.win.title("View")
        self.win.geometry("300x300")

        frame = Frame(self.win, bd=2, relief="sunken")
        frame.place(x=10, y=10, width=300, height=180)

        Button(frame,text="ورود حساب کاربری", command=self.show_view_customer).place(x=70, y=20)

        Button(frame, text="رزرو", command=self.show_view_reserve).place(x=80, y=60)



        self.win.mainloop()


ui = FrontView()
ui.show()
