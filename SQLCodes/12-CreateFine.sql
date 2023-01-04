USE [Traffic_Fines]
GO

/****** Object:  Table [dbo].[tblFine]    Script Date: 1/4/2023 11:56:56 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tblFine](
	[Id] [int] NOT NULL,
	[PlateNum] [nvarchar](50) NOT NULL,
	[Date] [datetime] NOT NULL,
	[FineType] [nvarchar](50) NULL,
	[Cost] [int] NULL,
 CONSTRAINT [PK_tbl_fine] PRIMARY KEY CLUSTERED 
(
	[Id] ASC,
	[PlateNum] ASC,
	[Date] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[tblFine]  WITH CHECK ADD  CONSTRAINT [FK_tblFine_tblPerson] FOREIGN KEY([Id])
REFERENCES [dbo].[tblPerson] ([Id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[tblFine] CHECK CONSTRAINT [FK_tblFine_tblPerson]
GO

ALTER TABLE [dbo].[tblFine]  WITH CHECK ADD  CONSTRAINT [FK_tblFine_tblVehicle] FOREIGN KEY([PlateNum])
REFERENCES [dbo].[tblVehicle] ([PlateNum])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[tblFine] CHECK CONSTRAINT [FK_tblFine_tblVehicle]
GO