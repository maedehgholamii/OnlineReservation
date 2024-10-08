from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from controller.customer_controller import CustomerController
from view.component.label_text import TextWithLabel


class CustomerView:
    def reset_form(self):
        self.table.delete(*self.table.get_children())
        status, customer_list = CustomerController.find_all()
        if status:
            for customer in customer_list:
                self.table.insert("", END,
                                  values=(customer.id,customer.name, customer.family, customer.mobile,
                                          customer.instagram_id, customer.telegram_id))

    def save_click(self):
        status, result = CustomerController.save(self.name.variable.get(), self.family.variable.get(),
                                                 self.mobile.variable.get(), self.instagram_id.variable.get(),
                                                 self.telegram_id.variable.get())
        if status:
            entered_data = (
                f"Name: {self.name._variable.get()}\n"
                f"Family: {self.family._variable.get()}\n"
                f"Mobile: {self.mobile._variable.get()}\n"
                f"instagram_id: {self.instagram_id._variable.get()}\n"
                f"telegram_id: {self.telegram_id.get()}\n"
            )
            msg.showinfo("Customer Saved!", result)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def edit_click(self):
        status, result = CustomerController.edit(self.name.variable.get(), self.family.variable.get(),
                                                 self.mobile.variable.get(), self.instagram_id.variable.get(),
                                                 self.telegram_id.variable.get())
        if status:
            entered_data = (
                f"Name: {self.name._variable.get()}\n"
                f"Family: {self.family._variable.get()}\n"
                f"Mobile: {self.mobile._variable.get()}\n"
                f"instagram_id: {self.instagram_id._variable.get()}\n"
                f"telegram_id: {self.telegram_id.get()}\n"
            )
            msg.showinfo("Customer Edited!", result)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def remove_click(self):
        id = self.remove_row.variable.get()
        CustomerController.remove(id)
        msg.showinfo("Timing deleted!", f"Are you sure to delete {id}?")
        self.reset_form()


    def __init__(self):
        self.win = Tk()
        self.win.title("Customer View")
        self.win.geometry("900x450")

        self.id = TextWithLabel(self.win, "ID For ٍEdit: ", 20, 20)

        self.name = TextWithLabel(self.win, "Name", 20, 60)

        self.family = TextWithLabel(self.win, "Family", 20, 100)

        self.mobile = TextWithLabel(self.win, "Mobile", 20, 140)

        self.instagram_id = TextWithLabel(self.win, "Instagram Id", 20, 180)

        self.telegram_id = TextWithLabel(self.win, "Telegram Id", 20, 220)

        self.remove_row = TextWithLabel(self.win, "ID For Remove: ", 330, 400)


        Button(self.win, text= "save",activebackground = "light blue", command=self.save_click).place(x=90 , y=250, width = 50)
        Button(self.win, text= "edit",activebackground = "orange", command=self.edit_click).place(x=140 , y=250, width = 50)
        Button(self.win, text= "delete", activebackground = "red",command=self.remove_click).place(x=490 , y=400 , width = 50)

        self.table = ttk.Treeview(self.win, columns=(1,2,3,4,5,6), show="headings", height= 13)

        self.table.column(1, width=100)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=100)

        self.table.heading(1, text="id")
        self.table.heading(2, text="name")
        self.table.heading(3, text="family")
        self.table.heading(4, text=" mobile")
        self.table.heading(5, text="instagram_id")
        self.table.heading(6, text="telegram_id")

        self.table.place(x=320,y=20)

        self.reset_form()

        self.win.mainloop()