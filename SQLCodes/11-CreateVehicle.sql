USE [Traffic_Fines]
GO

/****** Object:  Table [dbo].[tblVehicle]    Script Date: 1/4/2023 11:58:22 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblVehicle](
	[PlateNum] [nvarchar](50) NOT NULL,
	[ViehcleType] [nvarchar](50) NULL,
	[ManufactorYear] [date] NULL,
 CONSTRAINT [PK_tbl_vehicle] PRIMARY KEY CLUSTERED 
(
	[PlateNum] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO