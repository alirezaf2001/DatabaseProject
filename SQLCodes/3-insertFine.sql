CREATE procedure [dbo].[insertfine]
(
@id int,
@Plate nvarchar(50),
@date datetime,
@FType nvarchar(50),
@cost int

)
as
begin
insert into tblFine(Id,PlateNum,Date,FineType,Cost)
values(@id,@Plate,@date,@FType,@cost)