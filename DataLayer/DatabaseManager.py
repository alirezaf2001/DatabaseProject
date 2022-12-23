import pyodbc

SERVER = 'DESKTOP-U1AVMOL'
DATABASE = 'Traffic_Fines'

# SERVER = DESKTOP-S2P20AR
# DATABASE = databasename

connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'
connection = pyodbc.connect(connection_string)

class dbManage():
    def __init__(self) -> None:
        self.cursor = connection.cursor()

    def exeQuery(self, query):
        self.cursor.execute(query)      
        data = self.cursor.fetchall()
        return data
