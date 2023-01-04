CREATE procedure [dbo].[updatefine]
(

@oldId int,
@oldPlate nvarchar(50),
@oldDate datetime,


@id int,
@Plate nvarchar(50),
@date datetime,
@FType nvarchar(50),
@cost int

)
as
begin
update tblFine set FineType=@FType,Cost=@cost, PlateNum=@Plate , Id=@id ,  Date=@date
where PlateNum=@oldPlate and Id=@oldId and Date=@oldDate