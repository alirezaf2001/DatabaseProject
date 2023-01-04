CREATE procedure [dbo].[updateuser]
(
@oldId int,
@I int,
@First nvarchar(50),
@Last nvarchar(50),
@photo varbinary(max),
@photoExtention varchar(10)
)
as
begin
update tblPerson set Id=@I, FirstName=@First,LastName=@Last,Photo=@photo, PhotoExtention= @photoExtention
where Id=@oldId