use TripOut_test
go

If (object_id('vETLHarmonogram') is not null) Drop view vETLHarmonogram;
go
CREATE VIEW vETLHarmonogram
AS
SELECT
	FK_Wycieczka = dbo.Wycieczka.IdWycieczki,
	FK_Atrakcja = dbo.Atrakcja.IdAtrakcji
FROM TripOutDB.dbo.Harmonogram as ST1
JOIN dbo.Wycieczka on dbo.Wycieczka.BK_WycieczkaID = ST1.FK_Wycieczka
JOIN TripOutDB.dbo.AtrakcjaDodatkowa ST2 on ST2.IdAtrakcjaDodatkowa = ST1.FK_AtrakcjaDodatkowa
JOIN dbo.Atrakcja on dbo.Atrakcja.Nazwa = ST2.NazwaAtrakcji
; 
go

MERGE INTO Harmonogram as TT
	USING vETLHarmonogram as ST
		ON TT.FK_Wycieczka = ST.FK_Wycieczka
		AND TT.FK_Atrakcja = ST.FK_Atrakcja
			WHEN Not Matched
				THEN
					INSERT
					Values (
					ST.FK_Wycieczka,
					ST.FK_Atrakcja
					)
			;

Drop view vETLHarmonogram;