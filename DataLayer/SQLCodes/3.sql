select Photo ,PlateNum,sum(Cost)
from tblPerson,tblFine
where tblperson.id= tblFine.id and tblPerson.id=@id
group by Photo,PlateNum