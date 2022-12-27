from DataLayer import DatabaseManager 

class tblPerson_LogicLayer:
    def __init__(self) -> None:
        self.db = DatabaseManager.dbManage()

    def select_all(self):
        data = self.db.exeQuery("SELECT * FROM tblPerson")
        return data
    def update(self,id,firstname,lastname,photo):
        self.db.exeQuery(f"EXEC updateuser {id} N'{firstname}' N'{lastname}' {photo} ")
         
    def insert(self,id,firstname,lastname,photo):
        self.db.exeQuery(f"EXEC insertuser {id} N'{firstname}' N'{lastname}' {photo} ")
        
               
    def delete(self,firstname,lastname,platenum,date,finetype,cost):
        self.db.exeQuery(f" EXEC DELETE {date} N'{firstname}' N'{lastname}' {platenum} N'{finetype}' '{cost}'")
        