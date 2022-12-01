from ..DataLayer import DatabaseManager



class tbl_person_LogicLayer:
    def __init__(self) -> None:
        self.db = DatabaseManager.dbManage()

    def select_all(self):
        data = self.db.exeQuery("SELECT * FROM tbl_person")