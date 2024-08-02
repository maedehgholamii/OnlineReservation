from controller.employee_controller import EmployeeController
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from view.component.label_text import TextWithLabel


class EmployeeView:
    def reset_form(self):
        self.table.delete(*self.table.get_children())
        status, employee_list = EmployeeController.find_all()
        if status:
            for employee in employee_list:
                self.table.insert("", END, values=(employee.id, employee.name, employee.family, employee.mobile, employee.instagram_id, employee.telegram_id))

    def save_click(self):
        status_value = self.status.variable.get()  # مقدار وضعیت انتخاب شده
        status_bool = True if status_value == "True" else False  # تبدیل به مقدار منطقی
        status, result = EmployeeController.save(self.name.variable.get(), self.family.variable.get(),self.mobile.variable.get(), self.instagram_id.variable.get(),self.telegram_id.variable.get(),status_bool)
        if status:
            msg.showinfo("Save",f"Employee saved? \n {result}")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def edit(self):
        status_value = self.status.variable.get()  # مقدار وضعیت انتخاب شده
        status_bool = True if status_value == "True" else False  # تبدیل به مقدار منطقی
        result = EmployeeController.edit(self.id.variable.get(), self.name.variable.get(), self.family.variable.get(), self.mobile.variable.get(), self.instagram_id.variable.get(), self.telegram_id.variable.get(), status_bool)
        if result:
            msg.showinfo("Edit",f"Employee edited? \n {result}")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def remove(self):
        id = self.remove_row.variable.get()
        EmployeeController.remove(id)
        msg.showinfo("Employee deleted!", f"Are you sure to delete {id}?")
        self.reset_form()

    def __init__(self):
        self.win = Tk()
        self.win.title("Employee View")
        self.win.geometry("1000x450")

        self.id = TextWithLabel(self.win, "ID For Edit: ", 20, 20)

        self.name = TextWithLabel(self.win, "Name ", 20, 60)

        self.family = TextWithLabel(self.win, "Family : ", 20, 100)

        self.mobile = TextWithLabel(self.win, "Mobile ", 20, 140)

        self.instagram_id = TextWithLabel(self.win, "Instagram Id ", 20, 180)

        self.telegram_id = TextWithLabel(self.win, "Telegram Id ", 20, 220)

        self.status = TextWithLabel(self.win, "Status: ", 20, 300)

        self.remove_row = TextWithLabel(self.win, "ID For Remove: ", 330, 260)

        Button(self.win, text= "save", command=self.save_click).place(x=90 , y=350, width = 50)

        Button(self.win, text= "edit", command=self.edit).place(x=160 , y=350 , width = 50)

        Button(self.win, text= "remove", command=self.remove).place(x=630 , y=260, width = 50)

        self.table = ttk.Treeview(self.win, columns=(1, 2, 3, 4, 5, 6, 7), show="headings")

        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=100)
        self.table.column(7, width=100)

        self.table.heading(1, text="id")
        self.table.heading(2, text="Name")
        self.table.heading(3, text="Family")
        self.table.heading(4, text="Mobile")
        self.table.heading(5, text="Instagram Id")
        self.table.heading(6, text="Telegram id")
        self.table.heading(7, text="Status")

        self.table.place(x=320,y=20)

        self.reset_form()

        self.win.mainloop()