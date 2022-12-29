from DataLayer import DatabaseManager 
class tblFine_LogicLayer:

    def __init__(self) -> None:
        self.db = DatabaseManager.dbManage()

    def select_timefine(self,id,fromdate,todate):
        self.db.identify(f"select * from tblFine where id='{id }' and fromdate='{fromdate }' and todate <'{ todate}'")
        
    def select_all(self):
        data=self.db.exeQuery("SELECT * FROM tblFine ")
        return data
    
    def update(self,First,Last,Plate,date,FType,cost):
        self.db.updatefine(f"EXEC'{ First}' N'{ Last}'  N'{ Plate}'  N'{FType}'  N'{cost}'")
    
    def insert(self,First,Last,Plate,date,FType,cost):
        self.db.insertfine(f"EXEC'{ First}'  N'{ Last}' N'{ Plate}'  N'{FType}' N'{cost}'")
        
    def delete(self,First,Last,Plate,date,FType,cost):
        self.db.deletefine(f"EXEC'{ First}'  N'{ Last}' N'{ Plate}'  N'{FType}' N'{cost}'")    