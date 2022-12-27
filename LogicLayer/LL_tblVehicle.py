from ..DataLayer import DatabaseManager

class tblVehicle_logiclayer:
    def __init__(self) -> None:
        self.db = DatabaseManager.dbManage()

    def select_all(self):
        data = self.db.exeQuery("SELECT * FROM tblVerson")
        return data    
    def update(self,firstname,lastname,platenum,date,finetype,cost):
        self.db.exeQuery(f"EXEC updateuser {date} N'{firstname}' N'{lastname}' {platenum} N'{finetype}' '{cost}'")
         
    def insert(self,firstname,lastname,platenum,date,finetype,cost):
        self.db.exeQuery(f"EXEC insertuser {date} N'{firstname}' N'{lastname}' {platenum} N'{finetype}' '{cost}' ")
        
               
    def delete(self,firstname,lastname,platenum,date,finetype,cost):
        self.db.exeQuery(f" EXEC DELETE {date} N'{firstname}' N'{lastname}' {platenum} N'{finetype}' '{cost}'")
        
        