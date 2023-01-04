CREATE procedure [dbo].[plateEntrance]
(
@Plate nvarchar(50)
)
as
begin
select FirstName,LastName,SUM(Cost)
from tblPerson,tblFine
where tblPerson.id=tblFine.id and tblFine.PlateNum=@Plate
group by FirstName, LastName