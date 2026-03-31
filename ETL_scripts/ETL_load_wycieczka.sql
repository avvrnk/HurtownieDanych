use TripOutDW
go 

If (object_id('vETLDimWycieczkaData') is not null) Drop View vETLDimWycieczkaData;
go
CREATE VIEW vETLDimWycieczkaData
AS
SELECT DISTINCT
    [IdWycieczki] as [BK_WycieczkaID],
    [Kraj] as [Kraj],
    [Miasto] as [Miasto],
    [Typ] as [TypWycieczki],
    CASE 
        WHEN [Cena] < 112 THEN 1
        WHEN [Cena] BETWEEN 112 AND 184 THEN 2
        WHEN [Cena] BETWEEN 184 AND 256 THEN 3
        WHEN [Cena] BETWEEN 256 AND 328 THEN 4
        ELSE 5
    END AS [CenaKat]
FROM [TripOutDB].dbo.[Wycieczka];
go 

MERGE INTO Wycieczka as TT
    USING vETLDimWycieczkaData as ST
        ON TT.Kraj = ST.Kraj
        AND TT.Miasto = ST.Miasto
        AND TT.TypWycieczki = ST.TypWycieczki
        AND TT.CenaKat = ST.CenaKat
            WHEN Not Matched
                THEN
                    INSERT
                    Values (
                    ST.BK_WycieczkaID,
                    ST.Kraj,
                    ST.Miasto,
                    ST.TypWycieczki,
                    ST.CenaKat
                    )
            ;

Drop View vETLDimWycieczkaData;