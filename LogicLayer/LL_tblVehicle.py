import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
    )

mycursor = mydb.cursor()
    
def select_all(self):
    data = self.db.exeQuery("SELECT * FROM tblPerson")
        
def update_(self):
    sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
    mycursor.execute(sql)
    mydb.commit() 
   
def insert(self):
   
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)
    mydb.commit()
        
def delete_(self):
    sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
    mycursor.execute(sql)
    mydb.commit()