use TripOutDW
go

If (object_id('dbo.DataTmp') is not null) DROP TABLE dbo.DataTmp;
CREATE TABLE dbo.DataTmp(
    IdDaty integer,
    Data varchar(10) not null,
    Rok integer not null,
    Kwartal integer not null,
    Miesiac varchar(20) not null,
    MiesiacNum integer not null,
    Dzien integer not null,
    DzienTygodnia varchar(20) not null,
    DzienTygodniaNum integer not null,
    Wakacje bit not null,
    Sezon varchar(10) not null
);
go

BULK INSERT dbo.DataTmp
from 'C:\Users\wronk\projekty\HurtownieDanych\DB_TripOut_dane\dane\odczyt\daty.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 1, 
	CODEPAGE = 65001
	);
go

MERGE INTO dbo.Data AS TT
USING dbo.DataTmp AS ST
    ON TT.Data = ST.Data

WHEN NOT MATCHED THEN
    INSERT (
        Data,
        Rok,
        Kwartal,
        Miesiac,
        MiesiacNum,
        Dzien,
        DzienTygodnia,
        DzienTygodniaNum,
        Wakacje,
        Sezon
    )
    VALUES (
        ST.Data,
        ST.Rok,
        ST.Kwartal,
        ST.Miesiac,
        ST.MiesiacNum,
        ST.Dzien,
        ST.DzienTygodnia,
        ST.DzienTygodniaNum,
        ST.Wakacje,
        ST.Sezon
    );
GO

DROP TABLE dbo.DataTmp;