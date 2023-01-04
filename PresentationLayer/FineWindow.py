import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox as msg

from LogicLayer import LL_tblFine

from PresentationLayer import Add_EditFine
from PresentationLayer.Entities.Fine import Fine

class Window:
    def __init__(self, master) -> None:
        frameMaster1 = Frame(master)
        frameMaster1.pack(side='left', anchor='nw',padx=5,pady=5)

        frameMaster2 = Frame(master)
        frameMaster2.pack(side='left', anchor='nw',padx=5,pady=5)

        frame1 = Frame(frameMaster1)
        frame1.pack(side='top', anchor='nw',padx=5,pady=5)
        

        label = Label(frame1, text="کد ملی:")
        label.grid(row= 0, column= 0,ipadx=20,ipady=10, sticky='E')

        self.entry_id = Entry(frame1)
        self.entry_id.grid(row= 0, column= 1,ipadx=20,ipady=10, sticky='W')

        lable = Label(frame1, text="از تاریخ:")
        lable.grid(row= 0, column= 2,ipadx=20,ipady=10, sticky='E')

        self.entry_fromDate = Entry(frame1)
        self.entry_fromDate.grid(row= 0, column= 3,ipadx=20,ipady=10, sticky='W')

        lable = Label(frame1, text="تا تاریخ:")
        lable.grid(row= 0, column= 4,ipadx=20,ipady=10, sticky='E')

        self.entry_toDate = Entry(frame1)
        self.entry_toDate.grid(row= 0, column= 5,ipadx=20,ipady=10, sticky='W')

        button = Button(frame1, text="جست‌وجو",style='btnStyle.TButton', command=self.loadFilteredDate)
        button.grid(row= 0, column= 6,ipadx=5,ipady=5, sticky='E')

        frame2 = Frame(frameMaster1)
        frame2.pack(side='top', anchor='nw',padx=5,pady=5)

        cols = ('id','plateNum','date','fineType','cost')
        self.treeview = Treeview(frame2, columns=cols,selectmode='browse', show= 'headings')
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

        button = Button(frame2, text="بازرسانی",style='btnStyle.TButton',command=self.loadData)
        button.pack(side = 'top', anchor='nw',padx=5, pady=5, fill = 'both')

        self.loadData()

        frame3 = Frame(frameMaster2)
        frame3.pack(side='top',padx=5,pady=5)

        button = Button(frame3, text="جدید",style='btnStyle.TButton',command=self.openAddFineWindow)
        button.pack(side='top', anchor='ne',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(frame3, text="ویرایش",style='btnStyle.TButton',command=self.openEditFineWindow)
        button.pack(side='top', anchor='ne',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(frame3, text="خروج",style='btnStyle.TButton',command=master.destroy)
        button.pack(side='bottom', anchor='se',padx=5,pady=5,ipadx=50,ipady=10)

    def loadData(self):
        fine = LL_tblFine.tblFine_LogicLayer()
        data = fine.select_all()
        self.treeview.delete(*self.treeview.get_children())
        for index , row in enumerate(data):
            self.treeview.insert('', tk.END, text = row[0], values=(row[0],row[1],row[2],row[3],row[4]))
        
    def loadFilteredDate(self):
        id = self.entry_id.get()
        fromdate = self.entry_fromDate.get()
        todate = self.entry_toDate.get()
        fine = LL_tblFine.tblFine_LogicLayer()
        data = fine.show(id, fromdate , todate)
        self.treeview.delete(*self.treeview.get_children())
        for index , row in enumerate(data):
            self.treeview.insert('', tk.END, text = row[0], values=(row[0],row[1],row[2],row[3],row[4]))
        
    def openAddFineWindow(self):
        nextWindow = Add_EditFine.MainWindow()
        nextWindow.startWindow()

    def openEditFineWindow(self):
        itemId = self.treeview.focus()
        if itemId == '':
            msg.showerror(title="No item selected",message="لطفا یک ایتم را انتخاب کنید")
            return
        item = self.treeview.item(itemId)['values']
        llFine = LL_tblFine.tblFine_LogicLayer()
        finelst = llFine.select(item[0],item[1],item[2])[0]
        fine = Fine(
            finelst[0],
            finelst[1],
            finelst[2],
            finelst[3],
            finelst[4]
        )
        nextWindow = Add_EditFine.MainWindow(isNew=False, fine=fine)
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
        self.root.title('Fine')
        self.root.geometry("1200x500")
        self.root.mainloop()