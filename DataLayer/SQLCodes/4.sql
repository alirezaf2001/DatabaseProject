create procedure
(
@id int,
@fromdate datetime,
@todate datetime)
as 
begin
select *
from tblFine
where id=@id and date>@fromdate and date<@todate
end