use TripOutDW
go 

If (object_id('vETLFKwaterowanie') is not null) Drop view vETLFKwaterowanie;
go
CREATE VIEW vETLFKwaterowanie
AS
SELECT
    FK_Wycieczka = dbo.Wycieczka.IdWycieczki,
    FK_Hotelu = dbo.Hotel.IdHotelu
FROM TripOutDB.dbo.Kwaterowanie as KW
JOIN dbo.Wycieczka on dbo.Wycieczka.BK_WycieczkaID = KW.FK_Wycieczka
JOIN dbo.Hotel on dbo.Hotel.BKHotelu = KW.FK_Hotel
;
go

MERGE INTO Kwaterowanie as TT
    USING vETLFKwaterowanie as ST
        ON TT.FK_Wycieczka = ST.FK_Wycieczka
        AND TT.FK_Hotelu = ST.FK_Hotelu
            WHEN Not Matched
                THEN
                    INSERT
                    Values (
                    ST.FK_Wycieczka,
                    ST.FK_Hotelu
                    )
            ;
Drop view vETLFKwaterowanie;
