import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox as msg
import datetime

from PresentationLayer.Entities.Vehicle import Vehicle
from LogicLayer.LL_tblVehicle import tblVehicle_LogicLayer as llVehicle

class Window:
    def __init__(self, master, isNew = True, vehicle = Vehicle()) -> None:
        self.master = master
        self.isNew = isNew
        self.oldVehicle = vehicle
        frame1 = Frame(master)
        frame1.pack(side='top', anchor='nw',padx=5,pady=5)

        label = Label(frame1, text="شماره پلاک:")
        label.pack(side='left', anchor='center',padx=5,pady=5,ipadx=20,ipady=10)

        self.entry_plateNum = Entry(frame1)
        self.entry_plateNum.pack(side='left', anchor='center',padx=5,pady=5,ipadx=20,ipady=10)

        frame2 = Frame(master)
        frame2.pack(side='top', anchor='nw',padx=5,pady=5)

        lable = Label(frame2, text="نوع خودرو:")
        lable.pack(side='left', anchor='center',padx=5,pady=5,ipadx=22,ipady=10)

        self.entry_vehicleType = Entry(frame2)
        self.entry_vehicleType.pack(side='left', anchor='center',padx=5,pady=5,ipadx=20,ipady=10)

        frame3 = Frame(master)
        frame3.pack(side='top', anchor='nw',padx=5,pady=5)

        lable = Label(frame3, text="سال ساخت:")
        lable.pack(side='left', anchor='center',padx=5,pady=5,ipadx=22,ipady=10)

        self.entry_manufactorDate = Entry(frame3)
        self.entry_manufactorDate.pack(side='left', anchor='center',padx=5,pady=5,ipadx=20,ipady=10)

        frame4 = Frame(master)
        frame4.pack(side='right', anchor='se',padx=5,pady=5)

        button = Button(frame4, text="انصراف",style='btnStyle.TButton', command= master.destroy)
        button.pack(side='bottom', anchor='se',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(frame4, text="تایید",style='btnStyle.TButton',command=self.Insert_UpdateInfo)
        button.pack(side='bottom', anchor='se',padx=5,pady=5,ipadx=50,ipady=10)

        if not isNew:
            self.entry_plateNum.insert(0,vehicle.PlateNum) 
            self.entry_vehicleType.insert(0,vehicle.VehicleType) 
            self.entry_manufactorDate.insert(0,vehicle.ManufactorYear) 

    def Insert_UpdateInfo(self):
        try:
            temp = self.entry_manufactorDate.get()
            LogicVehicle = llVehicle()
            if self.isNew:
                LogicVehicle.insert(self.entry_plateNum.get(),
                                    self.entry_vehicleType.get(),
                                    self.entry_manufactorDate.get()
                                    )
            else:
                string = self.entry_manufactorDate.get()
                LogicVehicle.update(self.oldVehicle.PlateNum,
                                    self.entry_plateNum.get(),
                                    self.entry_vehicleType.get(),
                                    string
                                    )
            LogicVehicle.commit()
            msg.showinfo(title="success",message="عملیات با موفقیت انجام شد!")
            self.master.destroy()
        except Exception as err:
            msg.showerror(title="ERROR",message=err)

        
class MainWindow:
    def __init__(self,isNew = True, vehicle = None) -> None:
        self.root = tk.Tk()
        self.window = Window(self.root, isNew, vehicle)
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
            self.root.title('Add Vehicle')
        else:
            self.root.title('Edit Vehicle')
        self.root.geometry("800x500")
        self.root.mainloop()
