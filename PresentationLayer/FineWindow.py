import tkinter as tk
from tkinter.ttk import *

from LogicLayer import LL_tblVehicle

class Window:
    def __init__(self, master) -> None:
        frame = Frame(master)
        frame.pack(side='top', anchor='nw',padx=5,pady=5,ipadx=20,ipady=10)

        lable = Label(frame, text="کد ملی:")
        lable.pack(side='left', anchor='nw',padx=5,pady=5,ipadx=20,ipady=10)

        entry_id = Entry(frame)
        entry_id.pack(side='left', anchor='nw',padx=5,pady=5,ipadx=20,ipady=10)

        lable = Label(frame, text="از تاریخ:")
        lable.pack(side='left', anchor='nw',padx=5,pady=5,ipadx=20,ipady=10)

        entry_fromDate = Entry(frame)
        entry_fromDate.pack(side='left', anchor='nw',padx=5,pady=5,ipadx=20,ipady=10)

        lable = Label(frame, text="تا تاریخ:")
        lable.pack(side='left', anchor='nw',padx=5,pady=5,ipadx=20,ipady=10)

        entry_toDate = Entry(frame)
        entry_toDate.pack(side='left', anchor='nw',padx=5,pady=5,ipadx=20,ipady=10)

        cols = ('id','plateNum','date','fineType','cost')
        self.treeview = Treeview(master, columns=cols,selectmode='browse', show= 'headings')
        self.treeview.pack(side = 'left', anchor='nw',padx=5, pady=5, fill = 'both')

        self.treeview.column('id',anchor='center', stretch=False, width=80)
        self.treeview.heading('id', text="کد ملی")
        self.treeview.column('plateNum',anchor='center', stretch=False, width=180)
        self.treeview.heading('plateNum', text="شماره پلاک")
        self.treeview.column('date',anchor='center')
        self.treeview.heading('date', text="تاریخ صدور")
        self.treeview.column('fineType',anchor='center')
        self.treeview.heading('fineType', text="نوع جریمه")
        self.treeview.column('cost',anchor='center')
        self.treeview.heading('cost', text="مبلغ جریمه")

        self.loadData()

        button = Button(master, text="جدید",style='btnStyle.TButton')
        button.pack(side='top', anchor='ne',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(master, text="ویرایش",style='btnStyle.TButton')
        button.pack(side='top', anchor='ne',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(master, text="جست‌وجو",style='btnStyle.TButton')
        button.pack(side='top', anchor='ne',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(master, text="خروج",style='btnStyle.TButton',command=master.destroy)
        button.pack(side='bottom', anchor='se',padx=5,pady=5,ipadx=50,ipady=10)

    #TODO:Check if the select works
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
        self.root.geometry("1000x600")
        self.root.mainloop()