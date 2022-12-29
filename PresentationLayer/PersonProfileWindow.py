import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog
from PIL import Image, ImageTk

class Window:
    def __init__(self, master, isNew = False, person = None) -> None:
        infoFrame = Frame(master)
        infoFrame.pack(side='top', anchor='nw',padx=5,pady=5)

        self.pictureFrame = Frame(infoFrame)
        self.pictureFrame.pack(side='top', anchor='nw',padx=5,pady=5)

        self.imageLabel =Label(self.pictureFrame)
        self.imageLabel.pack(side='left', anchor='nw',padx=5,pady=5)
        

        personInfoFrame = Frame(infoFrame)
        personInfoFrame.pack(side='top', anchor='nw',padx=5,pady=5)
        
        label = Label(personInfoFrame, text="کد ملی:")
        label.grid(row = 0 , column= 0,ipadx=20,ipady=10)

        label = Label(personInfoFrame, text="123456789")
        label.grid(row = 0 , column= 1,ipadx=20,ipady=10)

        lable = Label(personInfoFrame, text="نام:")
        lable.grid(row = 1 , column= 0,ipadx=20,ipady=10)
        
        lable = Label(personInfoFrame, text="نام")
        lable.grid(row = 1 , column= 1,ipadx=20,ipady=10)

        lable = Label(personInfoFrame, text="نام خانوادگی:")
        lable.grid(row = 2 , column= 0,ipadx=20,ipady=10)

        lable = Label(personInfoFrame, text="نام خانوادگی")
        lable.grid(row = 2 , column= 1,ipadx=20,ipady=10)

    def LoadImage(self, image):
        #TODO: fix load image here
        self.newImage = Image.open()
        self.newImage = self.newImage.resize((150,200), Image.ANTIALIAS)
        self.python_newImage = ImageTk.PhotoImage(master = self.pictureFrame,image= self.newImage)
        self.imageLabel.configure(image=self.python_newImage)

        
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
