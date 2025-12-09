use TripOutDW
go

if (object_id('dbo.rezerwacje_temp') is not null) drop table dbo.rezerwacje_temp;
CREATE TABLE dbo.rezerwacje_temp
(
    Miasto varchar(100),
    Termin varchar(20),
    Cena varchar(20),
    LiczbaOsob varchar(20)
);
go 
BULK INSERT dbo.rezerwacje_temp
FROM 'C:\Users\wronk\projekty\HurtownieDanych\DB_TripOut_dane\dane\odczyt\rezerwacje.csv'
WITH
(
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',  
    ROWTERMINATOR = '\n',   
    TABLOCK
);

If (object_id('vETLOferta') is not null) Drop View vETLFOferta;
go
CREATE VIEW vETLFOferta
AS
SELECT
	d.IdDaty as IdDaty,
	w.IdWycieczki as IdWycieczki,
	p.IdPilota,
	t.DlugoscPobytu,
	t.IloscMiejsc,
	r.LiczbaOsob as ZarezerwowaneMiejsca,
	(wd.Cena * t.DlugoscPobytu) as CenaZaOsobe,
	CAST( r.LiczbaOsob as float) / t.IloscMiejsc as Oblozenie,
	(wd.Cena * t.DlugoscPobytu) * CAST(r.LiczbaOsob as int) as Przychod

FROM dbo.rezerwacje_temp as r 
join TripOutDB.dbo.Wycieczka as wd on wd.Miasto = r.Miasto and wd.Cena = r.Cena
join dbo.Wycieczka as w on w.BK_WycieczkaID = wd.IdWycieczki
join TripOutDB.dbo.Termin as t on t.DataWyjazdu = r.Termin and t.IdWycieczki = wd.IdWycieczki
join dbo.Data as d on d.Data = r.Termin
join TripOutDB.dbo.Pilot as wp on wp.IdPilota = wd.IdPilota
join dbo.Pilot as p on p.ImieNazwisko = CAST(wp.Imie + ' ' + wp.Nazwisko as nvarchar(128));

go 

MERGE INTO Oferta as TT
	USING vETLFOferta as ST
		ON
			TT.IdDaty = ST.IdDaty
		AND TT.IdWycieczki = ST.IdWycieczki 
		AND TT.IdPilota = ST.IdPilota
	    WHEN NOT MATCHED 
           AND ST.IdWycieczki IS NOT NULL
            THEN INSERT
                (
                    IdWycieczki,
                    IdDaty,
                    IdPilota,
                    DlugoscPobytu,
                    IloscMiejsc,
                    ZarezerwowaneMiejsca,
                    CenaZaOsobe,
                    Oblozenie,
                    Przychod
                )
                VALUES (
                    ST.IdWycieczki,
                    ST.IdDaty,
                    ST.IdPilota,
                    ST.DlugoscPobytu,
                    ST.IloscMiejsc,
                    ST.ZarezerwowaneMiejsca,
                    ST.CenaZaOsobe,
                    ST.Oblozenie,
                    ST.Przychod
                )

					;

drop view vETLFOferta;
drop table if exists dbo.rezerwacje_temp



    
