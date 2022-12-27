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
/*********/
create procedure insertfine
(
@id int,
@Plate nvarchar(50),
@date Datetime,
@FType nvarchar(50),
@cost int

)
as
begin
insert into tblFine(Id,PlateNum,Date,FineType,Cost)
values(@id,@Plate,@date,@FType,@cost)
end

/****************/
create procedure insertvehicle
(
@Plate nvarchar(50),
@VType nvarchar(50),
@MYear Datetime

)
as
begin
insert into tblVehicle(PlateNum,ViehcleType,ManufactorYear)
values(@Plate,@VType,@MYear)
end


/*update*/

create procedure updateuser
(

@I int,
@First nvarchar(50),
@Last nvarchar(50),
@photo varbinary(max)

)
as
begin
update tblPerson set FirstName=@First,LastName=@Last,Photo=@photo
where Id=@I
end

/**************/
create procedure updatevehicle
(

@Plate nvarchar(50),
@MYear Datetime,
@VType nvarchar(50),
@cost int

)
as
begin
update tblVehicle set PlateNum=@Plate,ViehcleType=-@VType,ManufactorYear=@MYear

end
/***********/
create procedure updatefine
(

@id int,
@Plate nvarchar(50),
@date Datetime,
@FType nvarchar(50),
@cost int

)
as
begin
update tblFine set PlateNum=@Plate,Date=@date,FineType=@FType,Cost=@cost
where Id=@id
end