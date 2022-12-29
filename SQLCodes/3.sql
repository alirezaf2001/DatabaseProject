create procedure identify
(
@id int,
@photo varbinary(max),
@Plate int,
@cost int
)
as
begin
select Photo ,PlateNum,sum(Cost)
from tblPerson,tblFine
where tblperson.id= tblFine.id and tblPerson.id=@id
group by Photo,PlateNum
end