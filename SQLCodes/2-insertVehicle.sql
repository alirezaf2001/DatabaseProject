CREATE procedure [dbo].[insertvehicle]
(
@Plate nvarchar(50),
@VType nvarchar(50),
@MYear date

)
as
begin
insert into tblVehicle(PlateNum,ViehcleType,ManufactorYear)
values(@Plate,@VType,@MYear)