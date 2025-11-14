INSERT INTO Data(IdDaty, Data, Rok, Kwartal, Miesiac, MiesiacNum, DzienTygodnia, DzienTygodniaNum, Wakacje, Sezon)
VALUES
(1,'2025-06-15',2025,2,'Czerwiec',6,'Niedziela',7,1,'Lato'),
(2,'2025-01-10',2025,1,'Styczeń',1,'Piątek',5,0,'Zima'),
(3,'2025-09-05',2025,3,'Wrzesień',9,'Piątek',5,0,'Lato'),
(4,'2025-12-22',2025,4,'Grudzień',12,'Poniedziałek',1,1,'Zima');

INSERT INTO Pilot(IdPilota, ImieNazwisko, Jezyk)
VALUES
(1, 'Adam Kowalski', 'Angielski'),
(2, 'Maria Nowak', 'Hiszpański'),
(3, 'Johann Müller', 'Niemiecki');

INSERT INTO Wycieczka(IdWycieczki, Kraj, Miasto, TypWycieczki, CenaKat)
VALUES
(1, 'Hiszpania', 'Barcelona', 'Wypoczynek', 3500),
(2, 'Włochy', 'Rzym', 'Zwiedzanie', 4100),
(3, 'Egipt', 'Hurghada', 'All-inclusive', 2900);

INSERT INTO Hotel(IdHotelu, BKHotelu, Nazwa, Adres, Kraj, Miasto, StandardHotelu, ZakresWyzywienia, 
                  LPokoi2os, LPokoi3os, LPokoi4os, UdogodnienieGlowne, Aktualny)
VALUES
(1, 101, 'Sun Resort', 'Calle Mar 21', 'Hiszpania', 'Barcelona', 4, 'All-inclusive', 40, 20, 10, 'Basen', 1),
(2, 102, 'Roma Palace', 'Via Roma 12', 'Włochy', 'Rzym', 5, 'Śniadania', 30, 10, 5, 'Spa', 1),
(3, 103, 'Desert Oasis', 'El-Hashimi 5', 'Egipt', 'Hurghada', 4, 'All-inclusive', 50, 25, 15, 'Prywatna plaża', 1);

INSERT INTO Atrakcja(IdAtrakcji, Nazwa, Typ)
VALUES
(1, 'Zwiedzanie Sagrady Familii', 'Kultura'),
(2, 'Rejs po Nilu', 'Rekreacja'),
(3, 'Koloseum – wycieczka z przewodnikiem', 'Kultura');

INSERT INTO Kwaterowanie(FK_Wycieczka, FK_Hotel)
VALUES
(1, 1),   -- Barcelona → Sun Resort
(2, 2),   -- Rzym → Roma Palace
(3, 3);   -- Hurghada → Desert Oasis

INSERT INTO Harmonogram(FK_Wycieczka, FK_Atrakcja)
VALUES
(1, 1),   -- Barcelona: Sagrada Familia
(2, 3),   -- Rzym: Koloseum
(3, 2);   -- Hurghada: rejs po Nilu

INSERT INTO Oferta(IdOferty, IdDaty, IdWycieczki, IdPilota, 
                    DlugoscPobytu, IloscMiejsc, ZarezerwowaneMiejsca,
                    CenaZaOsobe, Oblozenie, Przychod)
VALUES
(1, 1, 1, 1, 7, 40, 32, 3500.00, 80, 112000.00),
(2, 2, 2, 2, 5, 30, 22, 4100.00, 73, 90200.00),
(3, 3, 3, 3, 10, 50, 45, 2900.00, 90, 130500.00),
(4, 4, 1, 1, 7, 40, 20, 3500.00, 50, 70000.00);
