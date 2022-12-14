import tkinter as tk
from tkinter.ttk import *

from PresentationLayer import PersonWindow, VehicleWindow, FineWindow

class Window:
    def __init__(self, master) -> None:
        label = Label(master, text="سامانه تخلفات خودرو", font=('Arial',20,'bold'))
        label.pack(side='top',pady=10)
        
        Style().configure('btnStyle.TButton', font =('Arial', 14))

        button = Button(master, text="تخلفات",style='btnStyle.TButton', command=openFineWindow)
        button.pack(side='bottom',padx=5,pady=5,fill='x',ipady=10)

        button = Button(master, text="خودرو",style='btnStyle.TButton', command=openVehicleWindow)
        button.pack(side='bottom',padx=5,pady=5,fill='x',ipady=10)

        button = Button(master, text="افراد",style='btnStyle.TButton', command=openPersonWindow)
        button.pack(side='bottom',padx=5,pady=5,fill='x',ipady=10)
        
def openPersonWindow():
    nextWindow = PersonWindow.MainWindow()
    nextWindow.startWindow()

def openVehicleWindow():
    nextWindow = VehicleWindow.MainWindow()
    nextWindow.startWindow()

def openFineWindow():
    nextWindow = FineWindow.MainWindow()
    nextWindow.startWindow()

        

class MainWindow:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.window = Window(self.root)

    def startWindow(self):
        self.root.title('Vehicle Fines')
        self.root.geometry("300x400")
        self.root.mainloop()
