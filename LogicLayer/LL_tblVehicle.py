from DataLayer import DatabaseManager

class tblVehicle_LogicLayer:
    def __init__(self) -> None:
        self.db = DatabaseManager.dbManage()

    def select_all(self):
        data = self.db.exeQuery("SELECT * FROM tblVehicle")
        return data    
    
    def select(self, plateNum):
        data = self.db.exeQuery(f"SELECT * FROM tblVehicle WHERE PlateNum = N'{plateNum}'")
        return data

    def update(self,oldPlateNum,plateNum, VehicleType, ManufactorYear):
        self.db.exeQuery(f"EXEC updatevehicle ?,?,?,?",(oldPlateNum,plateNum,VehicleType,ManufactorYear))
         
    def insert(self,plateNum, VehicleType, ManufactorYear):
        self.db.exeQuery(f"EXEC insertvehicle ?,?,?",(plateNum,VehicleType,ManufactorYear))

    def commit(self):
        self.db.commit()
        
        