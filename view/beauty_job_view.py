from controller import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk

from controller.beauty_job_controller import BeautyJobController
from view.component.label_text import TextWithLabel


class BeautyJobView:
    def reset_form(self):
        status, beauty_job_list = BeautyJobController.find_all()
        if status:
            for beauty_job in beauty_job_list:
                self.table.insert("", END, values=(beauty_job.name, beauty_job.family, beauty_job.mobile, beauty_job.instagram_id, beauty_job.telegram_id))

    def save_click(self):
        status, result = BeautyJobController.save_beauty_job(self.title.get(), self.image.get(), self.description.get())
        if status:
            msg.showinfo("Beauty Job Saved!", result)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def edit_click(self):
        status, result = BeautyJobController.save_eauty_job(self.title.get(), self.image.get(), self.description.get())
        if status:
            msg.showinfo("Beauty Job Edited!", result)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)

    def remove_click(self):
        status, result = BeautyJobController.save_beauty_job(self.title.get(), self.image.get(), self.description.get())
        if status:
            msg.showinfo("Beauty Job Deleted!", result)
            self.reset_form()
        elif result.startswith("Error"):
            msg.showerror("Error", result)



    def show(self):
        self.win = Tk()
        self.win.title("Customer View")
        self.win.geometry("1000x400")

        name = TextWithLabel(self.win, "Title", 20, 20)

        family = TextWithLabel(self.win, "Image", 20, 60)

        mobile = TextWithLabel(self.win, "Description", 20, 100)




        Button(self.win, text= "save", command=self.save_click).place(x=20 , y=300)
        Button(self.win, text= "edit", command=self.edit_click).place(x=20 , y=340)
        Button(self.win, text= "delete", command=self.remove_click).place(x=20 , y=380)

        self.table = ttk.Treeview(self.win, columns=(1,2,3,4,5), show="headings")

        self.table.column(1, width=100)
        self.table.column(2, width=100)
        self.table.column(3, width=100)



        self.table.heading(1, text="title")
        self.table.heading(2, text="image")
        self.table.heading(3, text="descripion")


        self.table.place(x=320,y=20)

        self.reset_form()

        self.win.mainloop()