import tkinter as tk
from tkinter.ttk import *

from PresentationLayer.Entities.Vehicle import Vehicle

class Window:
    def __init__(self, master, isNew = True, vehicle = Vehicle()) -> None:
        frame1 = Frame(master)
        frame1.pack(side='top', anchor='nw',padx=5,pady=5)

        label = Label(frame1, text="شماره پلاک:")
        label.pack(side='left', anchor='center',padx=5,pady=5,ipadx=20,ipady=10)

        entry_plateNum = Entry(frame1)
        entry_plateNum.pack(side='left', anchor='center',padx=5,pady=5,ipadx=20,ipady=10)

        frame2 = Frame(master)
        frame2.pack(side='top', anchor='nw',padx=5,pady=5)

        lable = Label(frame2, text="نوع خودرو:")
        lable.pack(side='left', anchor='center',padx=5,pady=5,ipadx=22,ipady=10)

        entry_vehicleType = Entry(frame2)
        entry_vehicleType.pack(side='left', anchor='center',padx=5,pady=5,ipadx=20,ipady=10)

        frame3 = Frame(master)
        frame3.pack(side='top', anchor='nw',padx=5,pady=5)

        lable = Label(frame3, text="سال ساخت:")
        lable.pack(side='left', anchor='center',padx=5,pady=5,ipadx=22,ipady=10)

        entry_manufactorDate = Entry(frame3)
        entry_manufactorDate.pack(side='left', anchor='center',padx=5,pady=5,ipadx=20,ipady=10)

        frame4 = Frame(master)
        frame4.pack(side='right', anchor='se',padx=5,pady=5)

        button = Button(frame4, text="انصراف",style='btnStyle.TButton')
        button.pack(side='bottom', anchor='se',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(frame4, text="تایید",style='btnStyle.TButton')
        button.pack(side='bottom', anchor='se',padx=5,pady=5,ipadx=50,ipady=10)

        if not isNew:
            entry_plateNum.configure(textvariable=vehicle.PlateNum) 
            # entry_vehicleType = vehicle.VehicleType
            # entry_manufactorDate = vehicle.ManufactorYear



        
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
