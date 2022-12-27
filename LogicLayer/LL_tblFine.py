from DataLayer import DatabaseManager 
class tblFine_LogicLayer:

    def select_timefine(self,id,fromdate,todate):
        self.db.exeQuery(f"select * from tblFine where id='{id }' and fromdate='{fromdate }' and todate <'{ todate}'")
        
    def fname(self,First,Last,Plate,date,FType,cost):
        self.db.exeQuery(f"select * from tblFine where firstname='{ First}' and lastname='{ Last}' and plate='{ Plate}' and finetype='{FType}' and cost='{cost}'")
   
    
    def fname(arg):
        pass 
    
    def fname(arg):
        pass