from ..DataLayer import DatabaseManager



class tblPerson_LogicLayer:
    def __init__(self) -> None:
        self.db = DatabaseManager.dbManage()

    def select_all(self):
        data = self.db.exeQuery("SELECT * FROM tblPerson")
        
    def update_(self):
        data = self.db.exeQuery("SELECT * FROM tblPerson")    
   
    def insert(self):
        data = self.db.exeQuery("SELECT * FROM tblPerson") 
        
    def delete_(self):
        data = self.db.exeQuery("SELECT * FROM tblPerson")               