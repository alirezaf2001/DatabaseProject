import tkinter as tk
from tkinter.ttk import *


class Window:
    def __init__(self, master, isNew = False, person = None) -> None:
        infoFrame1 = Frame(master)
        infoFrame1.pack(side='top', anchor='nw',padx=5,pady=5)


        label = Label(infoFrame1, text="کد ملی:")
        label.pack(side='left', anchor='center',padx=5,pady=5,ipadx=20,ipady=10)

        entry_id = Entry(infoFrame1)
        entry_id.pack(side='left', anchor='center',padx=5,pady=5,ipadx=20,ipady=10)
        
        label = Label(infoFrame1, text="شماره پلاک:")
        label.pack(side='left', anchor='center',padx=5,pady=5,ipadx=20,ipady=10)

        entry_plateNum = Entry(infoFrame1)
        entry_plateNum.pack(side='left', anchor='center',padx=5,pady=5,ipadx=20,ipady=10)

        infoFrame2 = Frame(master)
        infoFrame2.pack(side='top', anchor='nw',padx=5,pady=5)

        lable = Label(infoFrame2, text="تاریخ:")
        lable.pack(side='left', anchor='center',padx=5,pady=5,ipadx=22,ipady=10)

        entry_date = Entry(infoFrame2)
        entry_date.pack(side='left', anchor='center',padx=5,pady=5,ipadx=20,ipady=10)

        lable = Label(infoFrame2, text="ساعت:")
        lable.pack(side='left', anchor='center',padx=5,pady=5,ipadx=22,ipady=10)

        entry_time = Entry(infoFrame2)
        entry_time.pack(side='left', anchor='center',padx=5,pady=5,ipadx=20,ipady=10)

        infoFrame3 = Frame(master)
        infoFrame3.pack(side='top', anchor='nw',padx=5,pady=5)

        lable = Label(infoFrame3, text="نوع تخلف:")
        lable.pack(side='left', anchor='center',padx=5,pady=5,ipadx=22,ipady=10)

        entry_fineType = Entry(infoFrame3)
        entry_fineType.pack(side='left', anchor='center',padx=5,pady=5,ipadx=20,ipady=10)

        lable = Label(infoFrame3, text="مبلغ:")
        lable.pack(side='left', anchor='center',padx=5,pady=5,ipadx=22,ipady=10)

        entry_cost = Entry(infoFrame3)
        entry_cost.pack(side='left', anchor='center',padx=5,pady=5,ipadx=20,ipady=10)

        buttonFrame = Frame(master)
        buttonFrame.pack(side='right', anchor='se',padx=5,pady=5)

        button = Button(buttonFrame, text="انصراف",style='btnStyle.TButton')
        button.pack(side='bottom', anchor='se',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(buttonFrame, text="تایید",style='btnStyle.TButton')
        button.pack(side='bottom', anchor='se',padx=5,pady=5,ipadx=50,ipady=10)



        
class MainWindow:
    def __init__(self,isNew = False, person = None) -> None:
        self.root = tk.Tk()
        self.window = Window(self.root, isNew, person)
        self.isNew = isNew

    def configStyle(self):
        self.style = Style(self.root)

        self.style.configure(
                        "Treeview",
                        rowheight = 40,
                        font = ('Arial',10))
        self.style.map("Treeview")

        self.style.configure(
                        'btnStyle.TButton',
                        font =('Arial', 13))
        
        self.style.configure(
                        'TLabel',
                        font =('Arial', 13)
        )

    def startWindow(self):
        self.configStyle()
        if self.isNew:
            self.root.title('Add Person')
        else:
            self.root.title('Edit Person')
        self.root.geometry("800x500")
        self.root.mainloop()
