select FirstName,LastName,PlateNum,Date,FineType,Cost
from tblPerson,tblFine
where tblPerson.id=tblFine.id and tblFine.PlateNum=@PlateNum