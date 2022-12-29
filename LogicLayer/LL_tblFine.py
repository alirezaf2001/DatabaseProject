from DataLayer import DatabaseManager 
class tblFine_LogicLayer:

    def __init__(self) -> None:
        self.db = DatabaseManager.dbManage()
        
    def select_all(self):
        data=self.db.exeQuery("SELECT * FROM tblFine ")
        return data
    
    def update(self,First,Last,Plate,date,FType,cost):
        self.db.exeQuery(f"EXEC update '{ First}' N'{ Last}'  N'{ Plate}' N'{date}' N'{FType}'  N'{cost}'")
    
    def insert(self,First,Last,Plate,date,FType,cost):
        self.db.exeQuery(f"EXEC insert '{ First}'  N'{ Last}' N'{ Plate}' N'{date}' N'{FType}' N'{cost}'")
        
    def delete(self,First,Last,Plate,date,FType,cost):
        self.db.exeQuery(f"EXEC delete '{ First}'  N'{ Last}' N'{ Plate}' N'{date}' N'{FType}' N'{cost}'")
        
    def identify(self,id):
        self.db.exeQuery(f"EXEC identify '{ id }' ")
        
    def show(self,id,fromdate,todate):
        self.db.exeQuery(f"EXEC show '{ id }' N'{ fromdate}' N'{ todate}' ")  
        
    def plateEntrance(self,Plate):
        self.db.exeQuery(f"EXEC plateEntrance '{ Plate }' ")    