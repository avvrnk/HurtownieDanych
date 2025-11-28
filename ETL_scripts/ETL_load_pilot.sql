use TripOut_test
go
If (object_id('vETLDimPilotData') is not null) Drop View vETLDimPilotData;
go
CREATE VIEW vETLDimPilotData
AS
SELECT DISTINCT
	[IdPilota] as [IdPilota],
	[ImieNazwisko] = Cast([Imie] + ' ' + [Nazwisko] as nvarchar(128)),
	[Jezyk] as [Jezyk]
FROM TripOutDB.dbo.Pilot;
go

MERGE INTO Pilot as TT
	USING vETLDimPilotData as ST
		ON TT.ImieNazwisko = ST.ImieNazwisko
			WHEN Not Matched
				THEN
					INSERT
					Values (
					ST.ImieNazwisko,
					ST.Jezyk
					)
			WHEN Not Matched By Source
				Then
					DELETE
			;

Drop View vETLDimPilotData;