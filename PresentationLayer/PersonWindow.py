import tkinter as tk
from tkinter.ttk import *

from LogicLayer import LL_tblPerson

from PresentationLayer import Add_EditPerson

class Window:
    def __init__(self, master) -> None:


        cols = ('id','firstName','lastName')
        self.treeview = Treeview(master, columns=cols,selectmode='browse', show= 'headings')
        self.treeview.pack(side = 'left', anchor='nw',padx=5, pady=5, fill = 'both')

        self.treeview.column('id',anchor='center', stretch=False, width=80)
        self.treeview.heading('id', text="کد ملی")
        self.treeview.column('firstName',anchor='center', stretch=False, width=180)
        self.treeview.heading('firstName', text="نام")
        self.treeview.column('lastName',anchor='center')
        self.treeview.heading('lastName', text="نام خانوادگی")

        self.loadData()

        button = Button(master, text="جدید",style='btnStyle.TButton', command=openAddPersonWindow)
        button.pack(side='top', anchor='ne',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(master, text="ویرایش",style='btnStyle.TButton')
        button.pack(side='top', anchor='ne',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(master, text="جست‌وجو",style='btnStyle.TButton')
        button.pack(side='top', anchor='ne',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(master, text="خروج",style='btnStyle.TButton',command=master.destroy)
        button.pack(side='bottom', anchor='se',padx=5,pady=5,ipadx=50,ipady=10)

    def loadData(self):
        person = LL_tblPerson.tblPerson_LogicLayer()
        data = person.select_all()
        for index , row in enumerate(data):
            self.treeview.insert('', tk.END, text = row[0], values=(row[0],row[1],row[2]))
        
def openAddPersonWindow():
    nextWindow = Add_EditPerson.MainWindow(isNew=True)
    nextWindow.startWindow()

def openWindow():
    pass

def openPersonWindow():
    pass

        

class MainWindow:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.window = Window(self.root)

    def configStyle(self):
        self.style = Style(self.root)

        self.style.configure(
                        "Treeview",
                        rowheight = 40,
                        font = ('Arial',10))
        self.style.map("Treeview")

        self.style.configure(
                        'btnStyle.TButton',
                        font =('Arial', 14))

        self.style.configure(
                        'TLabel',
                        font =('Arial', 13)
        )

    def startWindow(self):
        self.configStyle()
        self.root.title('Persons')
        self.root.geometry("800x500")
        self.root.mainloop()