from DataLayer import DatabaseManager 
class tblFine_LogicLayer:

    def select_timefine(self,id,fromdate,todate):
        self.db.exeQuery(f"select * from tblFine where id='{ }' and date='{ }' and date <'{ }'")