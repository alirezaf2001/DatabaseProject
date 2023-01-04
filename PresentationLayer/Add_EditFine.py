import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox as msg

from PresentationLayer.Entities.Fine import Fine
from LogicLayer.LL_tblFine import tblFine_LogicLayer as llFine
from LogicLayer.LL_tblPerson import tblPerson_LogicLayer as llPerson
from LogicLayer.LL_tblVehicle import tblVehicle_LogicLayer as llVehicle

class Window:
    def __init__(self, master, isNew = True, fine = Fine()) -> None:
        self.master = master
        self.isNew = isNew
        self.oldFine = fine
        infoFrame1 = Frame(master)
        infoFrame1.pack(side='top', anchor='nw',padx=5,pady=5)


        label = Label(infoFrame1, text="کد ملی:")
        label.grid(row= 0, column= 0,ipadx=20,ipady=10, sticky='W')

        self.cb_id = Combobox(infoFrame1)
        self.cb_id.grid(row= 0, column= 1,ipadx=20,ipady=10, sticky='W')
        
        label = Label(infoFrame1, text="شماره پلاک:")
        label.grid(row= 1, column= 0,ipadx=20,ipady=10, sticky='W')

        self.cb_plateNum = Combobox(infoFrame1)
        self.cb_plateNum.grid(row= 1, column= 1,ipadx=20,ipady=10, sticky='W')

        lable = Label(infoFrame1, text="تاریخ:")
        lable.grid(row= 2, column= 0,ipadx=20,ipady=10, sticky='W')

        self.entry_date = Entry(infoFrame1)
        self.entry_date.grid(row= 2, column= 1,ipadx=20,ipady=10, sticky='W')

        lable = Label(infoFrame1, text="ساعت:")
        lable.grid(row= 3, column= 0,ipadx=20,ipady=10, sticky='W')

        self.entry_time = Entry(infoFrame1)
        self.entry_time.grid(row= 3, column= 1,ipadx=20,ipady=10, sticky='W')

        lable = Label(infoFrame1, text="نوع تخلف:")
        lable.grid(row= 4, column= 0,ipadx=20,ipady=10, sticky='W')

        self.entry_fineType = Entry(infoFrame1)
        self.entry_fineType.grid(row= 4, column= 1,ipadx=20,ipady=10, sticky='W')

        lable = Label(infoFrame1, text="مبلغ:")
        lable.grid(row= 5, column= 0,ipadx=20,ipady=10, sticky='W')

        self.entry_cost = Entry(infoFrame1)
        self.entry_cost.grid(row= 5, column= 1,ipadx=20,ipady=10, sticky='W')

        buttonFrame = Frame(master)
        buttonFrame.pack(side='right', anchor='se',padx=5,pady=5)

        button = Button(buttonFrame, text="انصراف",style='btnStyle.TButton', command= master.destroy)
        button.pack(side='bottom', anchor='se',padx=5,pady=5,ipadx=50,ipady=10)

        button = Button(buttonFrame, text="تایید",style='btnStyle.TButton',command=self.Insert_UpdateInfo)
        button.pack(side='bottom', anchor='se',padx=5,pady=5,ipadx=50,ipady=10)

        self.LoadCombo()

        if not isNew:
            self.cb_id.set(fine.Id)
            self.cb_plateNum.set(fine.PlateNum)
            self.entry_fineType.insert(0,fine.FineType)
            self.entry_date.insert(0,fine.Date.date())
            self.entry_time.insert(0,fine.Date.time())
            self.entry_cost.insert(0,fine.Cost)

        

    def Insert_UpdateInfo(self):
        try:
            LogicFine = llFine()
            if self.isNew:

                LogicFine.insert(   int(self.cb_id.get().split()[0]),
                                    self.cb_plateNum.get().split()[0],
                                    str(self.entry_date.get()+" "+self.entry_time.get()),
                                    self.entry_fineType.get(),
                                    self.entry_cost.get()
                                    )
                
            else:
                LogicFine.update(   
                                    self.oldFine.Id,
                                    self.oldFine.PlateNum,
                                    self.oldFine.Date,
                                    int(self.cb_id.get().split()[0]),
                                    self.cb_plateNum.get().split()[0],
                                    str(self.entry_date.get()+" "+self.entry_time.get()),
                                    self.entry_fineType.get(),
                                    self.entry_cost.get()
                                    )
            LogicFine.commit()
            msg.showinfo(title="success",message="عملیات با موفقیت انجام شد!")
            self.master.destroy()
        except Exception as err:
            msg.showerror(title="ERROR",message=err)

    def LoadCombo(self):
        personLL = llPerson()
        vehicleLL = llVehicle()
        personLst = personLL.select_all()
        vehicleLst = vehicleLL.select_all()
        personCombo = []
        vehicleCombo = []

        for item in personLst:
            personCombo.append(str(str(item[0])+" "+item[1]+" "+item[2]))

        for item in vehicleLst:
            vehicleCombo.append(str(item[0]+" "+item[1]))
            
        self.cb_id['values'] = personCombo
        self.cb_plateNum['values'] = vehicleCombo

        
class MainWindow:
    def __init__(self,isNew = True, fine = None) -> None:
        self.root = tk.Tk()
        self.window = Window(self.root, isNew, fine)
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
            self.root.title('Add Fine')
        else:
            self.root.title('Edit Fine')
        self.root.geometry("800x500")
        self.root.mainloop()
