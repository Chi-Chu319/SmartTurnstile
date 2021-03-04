USE [Smart_turnstile]
GO

/****** Object:  StoredProcedure [dbo].[InsertAuthen]    Script Date: 2020/11/20 11:12:07 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[InsertAuthen] 
	-- Add the parameters for the stored procedure here
	@AuthenKey nvarchar(50),
	@BookingId int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	INSERT INTO dbo.Authen(AuthenKey,BookingId)
	VALUES(@AuthenKey, @BookingId)
END
GO


