from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from controller.beauty_job_controller import BeautyJobController
from view.component.label_text import TextWithLabel


class BeautyJobView:
    def reset_form(self):
        self.table.delete(*self.table.get_children())
        status, beauty_job_list = BeautyJobController.find_all()
        if status:
            for beauty_job in beauty_job_list:
                self.table.insert("", END, values=(beauty_job.name, beauty_job.family, beauty_job.mobile, beauty_job.instagram_id, beauty_job.telegram_id))

    def save(self):
        status, result = BeautyJobController.save_beauty_job(self.title.get(), self.image.get(), self.description.get())
        if status:
            msg.showinfo("Beauty Job Saved!", result)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def edit(self):
        status, result = BeautyJobController.save_beauty_job(self.title.get(), self.image.get(), self.description.get())
        if status:
            msg.showinfo("Beauty Job Edited!", result)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def remove(self):
        status, result = BeautyJobController.save_beauty_job(self.title.get(), self.image.get(), self.description.get())
        if status:
            msg.showinfo("Beauty Job Deleted!", result)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)



    def __init__(self):
        self.win = Tk()
        self.win.title("Customer View")
        self.win.geometry("800x300")

        self.title = TextWithLabel(self.win, "Title", 20, 20)

        self.image = TextWithLabel(self.win, "Image", 20, 60)

        self.description = TextWithLabel(self.win, "Description", 20, 100)




        Button(self.win, text= "save",activebackground = "light blue", command=self.save).place(x=90 , y=150, width = 50)
        Button(self.win, text= "edit",activebackground = "orange", command=self.edit).place(x=140 , y=150, width = 50)
        Button(self.win, text= "delete", activebackground = "red",command=self.remove).place(x=190 , y=150 , width = 50)

        self.table = ttk.Treeview(self.win, columns=(1,2,3), show="headings", height=10)

        self.table.column(1, width=100)
        self.table.column(2, width=100)
        self.table.column(3, width=200)



        self.table.heading(1, text="title")
        self.table.heading(2, text="image")
        self.table.heading(3, text="descripion")


        self.table.place(x=320,y=20)

        self.reset_form()

        self.win.mainloop()