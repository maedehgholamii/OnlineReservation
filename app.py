from view.customer_view import CustomerView
from view.employee_view import EmployeeView
from view.reserve_view import ReserveView
# print("App started")
# ui = PersonView()
# ui.show()
# print("App ended")

from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from view.component.label_text import TextWithLabel


class FrontView:

    def show_view_customer(self):
        msg.showinfo("question", "برای ایجاد حساب  ابتدا مشخصات خود را وارد کنید ")
        ui = CustomerView()
        ui.show()

    def show_view_reserve(self):
        ui = ReserveView()
        ui.show()

    def show(self):
        self.win = Tk()
        self.win.title("View")
        self.win.geometry("200x200")

        Button(self.win, text="ایجاد حساب کاربری", command=self.show_view_customer).place(x=20, y=20)

        Button(self.win, text="reserve", command=self.show_view_reserve).place(x=20, y=60)

        # self.table = ttk.Treeview(self.win, columns=(1,2), show="headings")

        # self.table.place(x=320, y=20)

        # self.reset_form()

        self.win.mainloop()


ui = CustomerView()
ui.show()