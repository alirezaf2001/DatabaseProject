from DataLayer import DatabaseManager 

class tblPerson_LogicLayer:
    def __init__(self) -> None:
        self.db = DatabaseManager.dbManage()

    def select_all(self):
        data = self.db.exeQuery("SELECT * FROM tblPerson")
        return data

    def select(self,id):
        data = self.db.exeQuery("SELECT * FROM tblPerson WHERE id = ?",(id))
        return data

    def update(self,oldId,id,firstname,lastname,photo,photoExtention):
        self.db.exeQuery(f"EXEC updateuser ?,?,?,?,?,?",(oldId,id,firstname,lastname,photo,photoExtention))
         
    def insert(self,id,firstname,lastname,photo,photoExtention):
        self.db.exeQuery("EXEC insertuser ?,?,?,?,?",(id,firstname,lastname,photo,photoExtention))
        
    def commit(self):
        self.db.commit()
        