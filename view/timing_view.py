from controller.timing_controller import TimingController
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from view.component.label_text import TextWithLabel


class TimingView:
    def reset_form(self):
        self.table.delete(*self.table.get_children())
        status, timing_list = TimingController.find_all()
        if status:
            for timing in timing_list:
                self.table.insert("", END, values=(timing.id, timing.shift_date,timing.start_time, timing.end_time))

    def save_click(self):
        status, result = TimingController.save(self.shift_date.variable.get(), self.start_time.variable.get(),self.end_time.variable.get())
        if status:
            msg.showinfo("Save",f"Timing saved? \n {result}")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def edit(self):
        result = TimingController.edit(self.id.variable.get(), self.shift_date.variable.get(), self.start_time.variable.get(), self.end_time.variable.get())
        if result:
            msg.showinfo("Edit",f"Timing edited? \n {result}")
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def remove(self):
        id = self.remove_row.variable.get()
        TimingController.remove(id)
        msg.showinfo("Timing deleted!", f"Are you sure to delete {id}?")
        self.reset_form()

    def __init__(self):
        self.win = Tk()
        self.win.title("Timing View")
        self.win.geometry("1000x450")

        self.id = TextWithLabel(self.win, "ID For Edit: ", 20, 20)

        self.shift_date = TextWithLabel(self.win, "Shift Date ", 20, 60)

        self.start_time = TextWithLabel(self.win, "Start Time : ", 20, 100)

        self.end_time = TextWithLabel(self.win, "End Time", 20, 140)

        self.remove_row = TextWithLabel(self.win, "ID For Remove: ", 330, 260)

        Button(self.win, text= "save", command=self.save_click).place(x=90 , y=350, width = 50)

        Button(self.win, text= "edit", command=self.edit).place(x=160 , y=350 , width = 50)

        Button(self.win, text= "remove", command=self.remove).place(x=630 , y=260, width = 50)

        self.table = ttk.Treeview(self.win, columns=(1, 2, 3, 4), show="headings")

        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)

        self.table.heading(1, text="id")
        self.table.heading(2, text="Shift Date")
        self.table.heading(3, text="Start Time")
        self.table.heading(4, text="End Time")

        self.table.place(x=320,y=20)

        self.reset_form()

        self.win.mainloop()