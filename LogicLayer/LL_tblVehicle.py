def select_all(self):
    data = self.db.exeQuery("SELECT * FROM tblPerson")
    return data    
def update_(self):
    self.db.exeQuery("UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'")
         
def insert(self):
    self.db.exeQuery("INSERT INTO customers (name, address) VALUES (%s, %s)")
        
               
def delete_(self):
    self.db.exeQuery("DELETE FROM customers WHERE address = 'Mountain 21'")
        