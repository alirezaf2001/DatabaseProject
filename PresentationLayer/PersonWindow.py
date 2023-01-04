import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox as msg
from tkinter import simpledialog as sd

from LogicLayer import LL_tblPerson

from PresentationLayer import Add_EditPerson , PersonProfileWindow
from PresentationLayer.Entities.Person import Person

class Window:
    def __init__(self, master) -> None:
        self.master = master

        cols = ('id','firstName','lastName')
        self.treeview = Treeview(master, columns=cols,selectmode='browse', show= 'headings')
        self.treeview.pack(side = 'left', anchor='nw',padx=5, pady=5, fill = 'both')

        self.treeview.column('id',anchor='center', stretch=False, width=80)
        self.treeview.heading('id', text="کد ملی")
        self.treeview.column('firstName',anchor='center', stretch=False, width=180)
        self.treeview.heading('firstName', text="نام")
        self.treeview.column('lastName',anchor='center')
        self.treeview.heading('lastName', text="نام خانوادگی")

        button = Button(master, text="بازرسانی",style='btnStyle.TButton', command=self.loadData)
        button.pack(side='left', anchor='ne',padx=5,pady=5,ipadx=5,ipady=5)

        self.loadData()

        button = Button(master, text="جدید",style='btnStyle.TButton', command=self.openAddPersonWindow)
        button.pack(side='top', anchor='ne',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(master, text="ویرایش",style='btnStyle.TButton',command=self.openEditPersonWindow)
        button.pack(side='top', anchor='ne',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(master, text="جست‌وجو",style='btnStyle.TButton', command=self.search)
        button.pack(side='top', anchor='ne',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(master, text="خروج",style='btnStyle.TButton',command=master.destroy)
        button.pack(side='bottom', anchor='se',padx=5,pady=5,ipadx=50,ipady=10)

    def loadData(self):
        llperson = LL_tblPerson.tblPerson_LogicLayer()
        data = llperson.select_all()
        self.treeview.delete(*self.treeview.get_children())
        for index , row in enumerate(data):
            self.treeview.insert('', tk.END, text = row[0], values=(row[0],row[1],row[2]))
        
    def openAddPersonWindow(self):
        nextWindow = Add_EditPerson.MainWindow()
        nextWindow.startWindow()

    def openEditPersonWindow(self):
        itemId = self.treeview.focus()
        if itemId == '':
            msg.showerror(title="No item selected",message="لطفا یک ایتم را انتخاب کنید")
            return
        item = self.treeview.item(itemId)['values']
        llPerson = LL_tblPerson.tblPerson_LogicLayer()
        personlst = llPerson.select(item[0])[0]
        person = Person(
            personlst[0],
            personlst[1],
            personlst[2],
            personlst[3],
            personlst[4]
        )
        nextWindow = Add_EditPerson.MainWindow(isNew=False,person=person)
        nextWindow.startWindow()

    def search(self):
        id = sd.askstring("Enter info","کد ملی را وارد کنید")
        llPerson = LL_tblPerson.tblPerson_LogicLayer()
        data = llPerson.select(id)
        if len(data) < 1:
            msg.showerror("ERROR","کد ملی مورد نظر در دیتابیس وجود ندارد!")
            return
        person = Person(
            data[0][0],
            data[0][1],
            data[0][2],
            data[0][3],
            data[0][4]
        )
        nextWindow = PersonProfileWindow.MainWindow(person)
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
        self.root.title('Persons')
        self.root.geometry("800x500")
        self.root.mainloop()