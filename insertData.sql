use TripOut
go


BULK INSERT Data 
from 'C:\Users\wronk\projekty\HurtownieDanych\lab4\sql\daty.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 1, 
	CODEPAGE = 65001
	);


INSERT INTO Pilot(IdPilota, ImieNazwisko, Jezyk)
VALUES
(1,'Adam Kowalski','Angielski'),
(2,'Maria Nowak','Hiszpański'),
(3,'Johann Müller','Niemiecki'),
(4,'Sara Lee','Angielski'),
(5,'Francesco Rossi','Włoski'),
(6,'Elena García','Hiszpański'),
(7,'Ahmed Hassan','Arabski'),
(8,'Pierre Dubois','Francuski'),
(9,'Emma Svensson','Szwedzki'),
(10,'Takeshi Yamamoto','Japoński');


INSERT INTO Wycieczka(IdWycieczki, Kraj, Miasto, TypWycieczki, CenaKat)
VALUES
(1,'Hiszpania','Barcelona','wypoczynkowa',3),
(2,'Włochy','Rzym','objazdowa',4),
(3,'Egipt','Hurghada','tematyczna',2),
(4,'Francja','Paryż','city-break',4),
(5,'Grecja','Ateny','objazdowa',3),
(6,'USA','Nowy Jork','city-break',5),
(7,'Japonia','Tokio','objazdowa',5),
(8,'Turcja','Antalya','wypoczynkowa',2),
(9,'Czechy','Praga','city-break',2),
(10,'Meksyk','Cancún','wypoczynkowa',4);


INSERT INTO Hotel(IdHotelu, BKHotelu, Nazwa, Adres, Kraj, Miasto, StandardHotelu,
                  ZakresWyzywienia, LPokoi2os, LPokoi3os, LPokoi4os, UdogodnienieGlowne, Aktualny)
VALUES
(1,101,'Sun Resort','Calle Mar 21','Hiszpania','Barcelona',4,'all-inclusive',40,20,10,'Basen',1),
(2,102,'Roma Palace','Via Roma 12','Włochy','Rzym',5,'śniadania',30,10,5,'Spa',1),
(3,103,'Desert Oasis','El-Hashimi 5','Egipt','Hurghada',4,'all-inclusive',50,25,15,'Prywatna plaża',1),
(4,104,'Eiffel Stay','Rue Lumière 33','Francja','Paryż',4,'2 posiłki',20,8,4,'Widok na wieżę Eiffla',1),
(5,105,'Acropolis Inn','Poseidon 7','Grecja','Ateny',3,'3 posiłki',25,12,6,'Blisko muzeum',1),
(6,106,'NYC Grand','5th Avenue 112','USA','Nowy Jork',5,'bez wyżywienia',60,20,10,'Siłownia',1),
(7,107,'Sakura Stay','Shibuya 2-11','Japonia','Tokio',5,'śniadania',45,15,5,'Onsen',1),
(8,108,'Antalya Beach','Ataturk 55','Turcja','Antalya',4,'all-inclusive',70,30,15,'Plaża',1),
(9,109,'Prague Center','Karlova 9','Czechy','Praga',3,'2 posiłki',35,10,4,'Centrum miasta',1),
(10,110,'Mayan Sun','Zona Hotelera 44','Meksyk','Cancún',5,'all-inclusive',80,35,20,'Basen infinity',1);

INSERT INTO Atrakcja(IdAtrakcji, Nazwa, Typ)
VALUES
(1,'Zwiedzanie Sagrady Familii','kultura'),
(2,'Rejs po Nilu','rekreacja'),
(3,'Koloseum – wycieczka z przewodnikiem','kultura'),
(4,'Wieża Eiffla – wjazd na szczyt','kultura'),
(5,'Akropol – zwiedzanie','kultura'),
(6,'Statua Wolności – rejs','rekreacja'),
(7,'Shibuya Crossing Tour','tematyczna'),
(8,'Rejs po Bosforze','rekreacja'),
(9,'Most Karola – historia','kultura'),
(10,'Chichén Itzá – wycieczka','kultura');


INSERT INTO Kwaterowanie(FK_Wycieczka, FK_Hotel)
VALUES
(1,1),(2,2),(3,3),(4,4),(5,5),
(6,6),(7,7),(8,8),(9,9),(10,10);


INSERT INTO Harmonogram(FK_Wycieczka, FK_Atrakcja)
VALUES
(1,1),(2,3),(3,2),(4,4),(5,5),
(6,6),(7,7),(8,8),(9,9),(10,10);


INSERT INTO Oferta(IdOferty, IdDaty, IdWycieczki, IdPilota,
                   DlugoscPobytu, IloscMiejsc, ZarezerwowaneMiejsca,
                   CenaZaOsobe, Oblozenie, Przychod)
VALUES
-- Barcelona
(1,77,1,1,7,40,32,3500,80,112000),
(2,6,1,4,7,40,28,3600,70,100800),
(3,45,1,6,7,40,35,3800,88,133000),

-- Rzym
(4,100,2,2,5,30,22,4500,73,99000),
(5,125,2,5,6,30,25,4200,83,105000),
(6,160,2,8,5,30,18,4800,60,86400),

-- Hurghada
(7,192,3,3,10,50,45,2500,90,112500),
(8,220,3,7,10,50,40,2700,80,108000),
(9,270,3,6,10,50,30,2900,60,87000),

-- Paryż
(10,290,4,8,4,20,15,4400,75,66000),
(11,310,4,8,4,20,18,4700,90,84600),

-- Ateny
(12,360,5,5,6,25,17,3300,68,56100),
(13,460,5,6,6,25,20,3400,80,68000),

-- Nowy Jork
(14,490,6,4,5,50,45,5200,90,234000),
(15,550,6,8,5,50,35,5500,70,192500),

-- Tokio
(16,610,7,10,8,40,25,6000,62,150000),
(17,766,7,10,8,40,30,6500,75,195000),

-- Antalya
(18,892,8,7,10,70,60,2200,85,132000),
(19,1542,8,3,10,70,55,2400,78,132000),

-- Praga
(20,2000,9,9,3,35,25,2100,71,52500),
(21,1992,9,9,3,35,30,2300,85,69000),

-- Cancún
(22,1666,10,1,10,80,50,4500,62,225000),
(23,1209,10,6,10,80,60,4700,75,282000),
(24,1487,10,8,10,80,70,4900,87,343000),

-- Dodatkowe mieszane
(25,1897,4,2,4,20,10,4100,50,41000),
(26,2180,5,5,6,25,15,3100,60,46500);
