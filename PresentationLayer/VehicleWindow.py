import tkinter as tk
from tkinter.ttk import *

from LogicLayer import LL_tblVehicle

class Window:
    def __init__(self, master) -> None:


        cols = ('plateNum','VehicleType','ManufactorYear')
        self.treeview = Treeview(master, columns=cols,selectmode='browse', show= 'headings')
        self.treeview.pack(side = 'left', anchor='nw',padx=5, pady=5, fill = 'both')

        self.treeview.column('plateNum',anchor='center', stretch=False, width=80)
        self.treeview.heading('plateNum', text="شماره پلاک")
        self.treeview.column('VehicleType',anchor='center', stretch=False, width=180)
        self.treeview.heading('VehicleType', text="نوع خودرو")
        self.treeview.column('ManufactorYear',anchor='center')
        self.treeview.heading('ManufactorYear', text="سال تولید")

        self.loadData()

        button = Button(master, text="جدید",style='btnStyle.TButton')
        button.pack(side='top', anchor='ne',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(master, text="ویرایش",style='btnStyle.TButton')
        button.pack(side='top', anchor='ne',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(master, text="جست‌وجو",style='btnStyle.TButton')
        button.pack(side='top', anchor='ne',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(master, text="خروج",style='btnStyle.TButton',command=master.destroy)
        button.pack(side='bottom', anchor='se',padx=5,pady=5,ipadx=50,ipady=10)

    def loadData(self):
        vehicle = LL_tblVehicle.tblVehicle_LogicLayer()
        data = vehicle.select_all()
        for index , row in enumerate(data):
            self.treeview.insert('', tk.END, text = row[0], values=(row[0],row[1],row[2]))
        
def openPersonWindow():
    pass

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

    def startWindow(self):
        self.configStyle()
        self.root.title('Persons')
        self.root.geometry("800x500")
        self.root.mainloop()