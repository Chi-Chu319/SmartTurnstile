-- ================================================
-- Template generated from Template Explorer using:
-- Create Procedure (New Menu).SQL
--
-- Use the Specify Values for Template Parameters 
-- command (Ctrl-Shift-M) to fill in the parameter 
-- values below.
--
-- This block of comments will not be included in
-- the definition of the procedure.
-- ================================================
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE SeedTheDatabase 
	-- Add the parameters for the stored procedure here

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	IF EXISTS (select 1 from dbo.Booking)
	Begin
	exec dbo.DeleteAllBookings
	end
	IF EXISTS (select 1 from dbo.Authen)
	Begin
	exec dbo.DeleteAllAuthens
	end
	Exec dbo.InsertBooking
		 @Name = 'Jonh',
		 @TIme = '20201112 11:22:43'
	Exec dbo.InsertBooking
		 @Name = 'Charleys',
		 @Time = '20201114 18:22:43'

	declare @id1 int,
			@id2 int

	set @id1 = 
	(select id from
	(
	select Id, ROW_NUMBER() OVER (ORDER BY Id) AS RowNum 
	from dbo.Booking
	) b
	where RowNum =1);

	set @id2 = 
	(select id from
	(
	select Id, ROW_NUMBER() OVER (ORDER BY Id) AS RowNum 
	from dbo.Booking
	) b
	where RowNum =2);

	Exec dbo.InsertAuthen
		@AuthenKey = 'key1',
		@BookingId = @id1
	Exec dbo.InsertAuthen
		@AuthenKey = 'key2',
		@BookingId = @id2


	


END
GO
