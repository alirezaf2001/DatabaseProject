CREATE procedure [dbo].[updatevehicle]
(
@oldPlate nvarchar(50),
@Plate nvarchar(50),
@VType nvarchar(50),
@MYear date

)
as
begin
update tblVehicle set PlateNum=@Plate, ViehcleType=@VType,ManufactorYear=@MYear
where PlateNum=@oldPlate