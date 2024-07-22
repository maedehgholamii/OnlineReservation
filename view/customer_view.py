from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk

from controller.customer_controller import CustomerController
from view.component.label_text import TextWithLabel


class CustomerView:
    def reset_form(self):
        status, customer_list = CustomerController.find_all()
        if status:
            for customer in customer_list:
                self.table.insert("", END, values=(customer.name, customer.family, customer.mobile, customer.instagram_id, customer.telegram_id))

    def save_click(self):
        status, result = CustomerController.save_customer(self.name.get(), self.family.get(), self.mobile.get(), self.instagram_id.get(),self.telegram_id.get())
        if status:
            msg.showinfo("Customer Saved!", result)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def show(self):
        self.win = Tk()
        self.win.title("Customer View")
        self.win.geometry("1100x400")

        name = TextWithLabel(self.win, "name: ", 20, 20)

        family = TextWithLabel(self.win, "family: ", 20, 60)

        mobile = TextWithLabel(self.win, "national id: ", 20, 100)

        instagram_id = TextWithLabel(self.win, "birthday: ", 20, 140)

        telegram_id = TextWithLabel(self.win, "phone: ", 20, 180)


        Button(self.win, text= "save", command=self.save_click).place(x=20 , y=340)

        self.table = ttk.Treeview(self.win, columns=(1,2,3,4,5,6), show="headings")

        self.table.column(1, width=100)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=120)


        self.table.heading(1, text="name")
        self.table.heading(2, text="family")
        self.table.heading(3, text=" mobile")
        self.table.heading(4, text="instagram_id")
        self.table.heading(5, text="telegram_id")

        self.table.place(x=320,y=20)

        self.reset_form()

        self.win.mainloop()