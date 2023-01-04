from DataLayer import DatabaseManager 
class tblFine_LogicLayer:

    def __init__(self) -> None:
        self.db = DatabaseManager.dbManage()
        
    def select_all(self):
        data=self.db.exeQuery("SELECT * FROM tblFine ")
        return data
    
    def select(self, id, plate, date):
        data = self.db.exeQuery(f"SELECT * FROM tblFine WHERE Id = {id} AND PlateNum = N'{plate}' AND Date = '{date}'")
        return data

    def update(self,oldId, oldPlate, oldDate,id,plate,date,ftype,cost):
        self.db.exeQuery(f"EXEC updatefine ?,?,?, ?,?,?,?,?",(oldId,oldPlate,oldDate,id,plate,date,ftype,cost))
    
    def insert(self,id,plate,date,ftype,cost):
        self.db.exeQuery(f"EXEC insertfine ?,?,?,?,?",(id,plate,date,ftype,cost))
        
    def identify(self,id):
        data = self.db.exeQuery(f"EXEC identify ?",(id))
        return data
        
    def show(self,id,fromdate,todate):
        data = self.db.exeQuery(f"EXEC show ?,?,?",(id,fromdate,todate))  
        return data
        
    def plateEntrance(self,Plate):
        data = self.db.exeQuery(f"EXEC plateEntrance ?",(Plate))    
        return data

    def commit(self):
        self.db.commit()
