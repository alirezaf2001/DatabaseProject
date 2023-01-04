import pyodbc

SERVER = 'DESKTOP-93OTLTM'
DATABASE = 'Traffic_Fines'

# SERVER = servername
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

    def exeQuery(self, query, *prams):
        self.cursor.execute(query, *prams)   
        try:
            data = self.cursor.fetchall()
            return data
        except:
            pass
    def commit(self):
        self.cursor.commit()