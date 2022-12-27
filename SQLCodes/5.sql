create procedure plateentrance
(
@First nvarchar(50),
@Last nvarchar(50),
@Plate int,
@date datetime,
@FType nvarchar(50),
@cost int
)
as
begin
select FirstName,LastName,PlateNum,Date,FineType,Cost
from tblPerson,tblFine
where tblPerson.id=tblFine.id and tblFine.PlateNum=@Plate
end