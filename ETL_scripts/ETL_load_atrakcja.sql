use TripOut_test
go
If (object_id('vETLDimAtrakcjaData') is not null) Drop View vETLDimAtrakcjaData;
go
CREATE VIEW vETLDimAtrakcjaData
AS
SELECT DISTINCT
	[IdAtrakcjaDodatkowa] as [IdAtrakcji] ,
	[NazwaAtrakcji] as [Nazwa],
	[Typ] as [Typ]
FROM TripOutDB.dbo.AtrakcjaDodatkowa;
go

MERGE INTO Atrakcja as TT
	USING vETLDimAtrakcjaData as ST
		ON TT.Nazwa = ST.Nazwa
			WHEN Not Matched
				THEN
					INSERT
					Values (
					ST.Nazwa,
					ST.Typ
					)
			WHEN Not Matched By Source
				Then
					DELETE
			;

Drop View vETLDimAtrakcjaData;