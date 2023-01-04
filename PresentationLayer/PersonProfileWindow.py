import tkinter as tk
from tkinter.ttk import *

from PresentationLayer.Entities.Person import Person
from LogicLayer.LL_tblFine import tblFine_LogicLayer

from PIL import Image, ImageTk

class Window:
    def __init__(self, master, person = Person()) -> None:
        infoFrame = Frame(master)
        infoFrame.pack(side='left', anchor='nw',padx=5,pady=5)

        self.fileName = person.Id
        self.fileExtention = person.PhotoExtention

        self.pictureFrame = Frame(infoFrame)
        self.pictureFrame.pack(side='top', anchor='nw',padx=5,pady=5)

        self.imageLabel =Label(self.pictureFrame)
        self.imageLabel.pack(side='left', anchor='nw',padx=5,pady=5)
        

        personInfoFrame = Frame(infoFrame)
        personInfoFrame.pack(side='top', anchor='nw',padx=5,pady=5)
        
        label = Label(personInfoFrame, text="کد ملی:")
        label.grid(row = 0 , column= 0,ipadx=20,ipady=10)

        label = Label(personInfoFrame, text=person.Id)
        label.grid(row = 0 , column= 1,ipadx=20,ipady=10)

        lable = Label(personInfoFrame, text="نام:")
        lable.grid(row = 1 , column= 0,ipadx=20,ipady=10)
        
        lable = Label(personInfoFrame, text=person.FirstName)
        lable.grid(row = 1 , column= 1,ipadx=20,ipady=10)

        lable = Label(personInfoFrame, text="نام خانوادگی:")
        lable.grid(row = 2 , column= 0,ipadx=20,ipady=10)

        lable = Label(personInfoFrame, text=person.LastName)
        lable.grid(row = 2 , column= 1,ipadx=20,ipady=10)

        self.LoadImage(person.Photo, person)

        fineInfoFrame = Frame(master)
        fineInfoFrame.pack(side='left', anchor='nw',padx=5,pady=5)

        cols = ('plate','cost')
        self.treeview = Treeview(fineInfoFrame, columns=cols,selectmode='browse', show= 'headings')
        self.treeview.pack(side = 'left', anchor='nw',padx=5, pady=5, fill = 'both')

        self.treeview.column('plate',anchor='center', stretch=False, width=80)
        self.treeview.heading('plate', text="شماره پلاک")
        self.treeview.column('cost',anchor='center', stretch=False, width=100)
        self.treeview.heading('cost', text="مجموع جریمه")

        self.LoadTable(person.Id)

    def LoadImage(self, image, person = Person()):
        path = save_image(image, person.Id, person.PhotoExtention)
        self.newImage = Image.open(path)
        self.newImage = self.newImage.resize((150,200), Image.ANTIALIAS)
        self.python_newImage = ImageTk.PhotoImage(master = self.pictureFrame,image= self.newImage)
        self.imageLabel.configure(image=self.python_newImage)

    def LoadTable(self, id):
        llfine = tblFine_LogicLayer()
        data = llfine.identify(id)
        self.treeview.delete(*self.treeview.get_children())
        for index , row in enumerate(data):
            self.treeview.insert('', tk.END, text = row[0], values=(row[1],row[2]))

def save_image(image, file_name, file_Extention):
    with open(f"Resources/temp/{file_name}.{file_Extention}", 'wb') as file:
        file.write(image) 
    return f"Resources/temp/{file_name}.{file_Extention}"
        
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
        self.root.title('Person Profile')
        self.root.geometry("800x500")
        self.root.mainloop()
