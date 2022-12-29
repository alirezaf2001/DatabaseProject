import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog
from PIL import Image, ImageTk

class Window:
    def __init__(self, master, isNew = False, person = None) -> None:
        self.frame1 = Frame(master)
        self.frame1.pack(side='left', anchor='nw',padx=5,pady=5)

        self.imageLabel =Label(self.frame1)
        self.imageLabel.grid(row= 0, column= 0, padx=5, pady=5)   

        button = Button(self.frame1, text="انتخاب عکس",style='btnStyle.TButton',command=self.Select_file)
        button.grid(row= 0, column= 0, padx=5, pady=5, sticky='W,E,S')
        self.newImage = Image.new('RGB', (150, 200))
        self.python_newImage = ImageTk.PhotoImage(master = self.frame1,image= self.newImage)
        self.imageLabel.configure(image=self.python_newImage)

        frame2 = Frame(master)
        frame2.pack(side='left', anchor='nw',padx=5,pady=5)

        label = Label(frame2, text="کد ملی:")
        label.grid(row= 0, column= 0,ipadx=20,ipady=10, sticky='W')

        entry_id = Entry(frame2)
        entry_id.grid(row= 0, column= 1,ipadx=20,ipady=10, sticky='W')

        lable = Label(frame2, text="نام:")
        lable.grid(row= 1, column= 0,ipadx=20,ipady=10, sticky='W')

        entry_firstName = Entry(frame2)
        entry_firstName.grid(row= 1, column= 1,ipadx=20,ipady=10, sticky='W')

        lable = Label(frame2, text="نام خانوادگی:")
        lable.grid(row= 2, column= 0,ipadx=20,ipady=10, sticky='W')

        entry_lastName = Entry(frame2)
        entry_lastName.grid(row= 2, column= 1,ipadx=20,ipady=10, sticky='W')

        buttonFrame = Frame(master)
        buttonFrame.pack(side='right', anchor='se',padx=5,pady=5)

        button = Button(buttonFrame, text="انصراف",style='btnStyle.TButton')
        button.pack(side='bottom', anchor='se',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(buttonFrame, text="تایید",style='btnStyle.TButton')
        button.pack(side='bottom', anchor='se',padx=5,pady=5,ipadx=50,ipady=10)

    def Select_file(self):
        filetypes = (
        ('Image files', '*.png'),
        ('Image files', '*.jpg'),
        ('All files', '*.*')
        )
        fileName = filedialog.askopenfilename(
            title ='Select an image',
            initialdir = '/',
            filetypes = filetypes
        )
        self.newImage = Image.open(fileName)
        self.newImage = self.newImage.resize((150,200), Image.ANTIALIAS)
        self.python_newImage = ImageTk.PhotoImage(master = self.frame1,image= self.newImage)
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
