import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox as msg
from tkinter import simpledialog as sd

from LogicLayer import LL_tblVehicle

from PresentationLayer import Add_EditVehicle , VehicleProfileWindow
from PresentationLayer.Entities.Vehicle import Vehicle
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

        button = Button(master, text="بازرسانی",style='btnStyle.TButton', command=self.loadData)
        button.pack(side='left', anchor='ne',padx=5,pady=5,ipadx=5,ipady=5)

        self.loadData()

        button = Button(master, text="جدید",style='btnStyle.TButton',command=self.openAddVehicleWindow)
        button.pack(side='top', anchor='ne',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(master, text="ویرایش",style='btnStyle.TButton',command=self.openEditVehicleWindow)
        button.pack(side='top', anchor='ne',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(master, text="جست‌وجو",style='btnStyle.TButton',command=self.search)
        button.pack(side='top', anchor='ne',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(master, text="خروج",style='btnStyle.TButton',command=master.destroy)
        button.pack(side='bottom', anchor='se',padx=5,pady=5,ipadx=50,ipady=10)

    def loadData(self):
        llvehicle = LL_tblVehicle.tblVehicle_LogicLayer()
        data = llvehicle.select_all()
        self.treeview.delete(*self.treeview.get_children())
        for index , row in enumerate(data):
            self.treeview.insert('', tk.END, text = row[0], values=(row[0],row[1],row[2]))
        
    def openAddVehicleWindow(self):
        nextWindow = Add_EditVehicle.MainWindow()
        nextWindow.startWindow()

    def openEditVehicleWindow(self):
        itemId = self.treeview.focus()
        if itemId == '':
            msg.showerror(title="No item selected",message="لطفا یک ایتم را انتخاب کنید")
            return
        item = self.treeview.item(itemId)['values']
        llVehicle = LL_tblVehicle.tblVehicle_LogicLayer()
        vehiclelst = llVehicle.select(item[0])[0]
        vehicle = Vehicle(
            vehiclelst[0],
            vehiclelst[1],
            vehiclelst[2]
        )
        nextWindow = Add_EditVehicle.MainWindow(isNew= False, vehicle= vehicle)
        nextWindow.startWindow()

    def search(self):
        id = sd.askstring("Enter info","شماره پلاک را وارد کنید")
        llVehicle = LL_tblVehicle.tblVehicle_LogicLayer()
        data = llVehicle.select(id)
        if len(data) < 1:
            msg.showerror("ERROR","خودرو مورد نظر در دیتابیس وجود ندارد!")
            return
        
        vehicle = Vehicle(
            data[0][0],
            data[0][1],
            data[0][2]
        )
        nextWindow = VehicleProfileWindow.MainWindow(vehicle)
        nextWindow.startWindow()      

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
        self.root.title('Vehicle')
        self.root.geometry("800x500")
        self.root.mainloop()