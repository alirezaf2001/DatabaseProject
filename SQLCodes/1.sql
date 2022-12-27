create procedure insertuser
(
@I int,
@First nvarchar(50),
@Last nvarchar(50),
@photo varbinary(max)
)
as
begin
insert into tblPerson(Id,FirstName,LastName,Photo)
values(@I,@First,@Last,@photo)
end 

create procedure insertfine
(
@id int,
@Plate nvarchar(50),
@Date Datetime,
@FType nvarchar(50),
@cost int

)
as
begin
insert into tblFine(Id,PlateNum,Date,FineType,Cost)
values(@id,@Plate,@Date,@FType,@cost)
end