import tkinter as tk
from tkinter.ttk import *

from PresentationLayer.Entities.Vehicle import Vehicle
from LogicLayer.LL_tblFine import tblFine_LogicLayer

class Window:
    def __init__(self, master, vehicle = Vehicle()) -> None:
        infoFrame = Frame(master)
        infoFrame.pack(side='left', anchor='nw',padx=5,pady=5)
        
        label = Label(infoFrame, text="شماره پلاک:")
        label.grid(row = 0 , column= 0,ipadx=20,ipady=10)

        label = Label(infoFrame, text=vehicle.PlateNum)
        label.grid(row = 0 , column= 1,ipadx=20,ipady=10)

        lable = Label(infoFrame, text="نوع خودرو:")
        lable.grid(row = 1 , column= 0,ipadx=20,ipady=10)
        
        lable = Label(infoFrame, text=vehicle.VehicleType)
        lable.grid(row = 1 , column= 1,ipadx=20,ipady=10)

        lable = Label(infoFrame, text="سال ساخت:")
        lable.grid(row = 2 , column= 0,ipadx=20,ipady=10)

        lable = Label(infoFrame, text=vehicle.ManufactorYear.year)
        lable.grid(row = 2 , column= 1,ipadx=20,ipady=10)

        fineInfoFrame = Frame(master)
        fineInfoFrame.pack(side='left', anchor='nw',padx=5,pady=5)

        cols = ('firstname','lastname','cost')
        self.treeview = Treeview(fineInfoFrame, columns=cols,selectmode='browse', show= 'headings')
        self.treeview.pack(side = 'left', anchor='nw',padx=5, pady=5, fill = 'both')

        self.treeview.column('firstname',anchor='center', stretch=False, width=150)
        self.treeview.heading('firstname', text="نام")
        self.treeview.column('lastname',anchor='center', stretch=False, width=150)
        self.treeview.heading('lastname', text="نام خانوادگی")
        self.treeview.column('cost',anchor='center', stretch=False, width=100)
        self.treeview.heading('cost', text="مبلغ جریمه")

        self.LoadTable(vehicle.PlateNum)

    def LoadTable(self, plateNum):
        llfine = tblFine_LogicLayer()
        data = llfine.plateEntrance(plateNum)
        self.treeview.delete(*self.treeview.get_children())
        for index , row in enumerate(data):
            self.treeview.insert('', tk.END, text = row[0], values=(row[0],row[1],row[2]))
        
class MainWindow:
    def __init__(self, person = None) -> None:
        self.root = tk.Tk()
        self.window = Window(self.root, person)


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
        self.root.title('Vehicle Profile')
        self.root.geometry("800x500")
        self.root.mainloop()
