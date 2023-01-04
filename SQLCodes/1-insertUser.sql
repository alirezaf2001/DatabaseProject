CREATE procedure [dbo].[insertuser]
(
@I int,
@First nvarchar(50),
@Last nvarchar(50),
@photo varbinary(max),
@photoExtention varchar(10)
)
as
begin
insert into tblPerson(Id,FirstName,LastName,Photo,PhotoExtention)
values(@I,@First,@Last,@photo,@photoExtention)