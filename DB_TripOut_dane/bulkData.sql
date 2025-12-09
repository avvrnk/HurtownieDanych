use TripOutDB				-- HD_biuroPodró¿y
go 

BULK INSERT Pilot 
from 'C:\Users\wronk\projekty\HurtownieDanych\DB_TripOut_dane\dane\odczyt\piloci.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT Wycieczka 
from 'C:\Users\wronk\projekty\HurtownieDanych\DB_TripOut_dane\dane\odczyt\wycieczki.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT Termin 
from 'C:\Users\wronk\projekty\HurtownieDanych\DB_TripOut_dane\dane\odczyt\terminy.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT Hotel 
from 'C:\Users\wronk\projekty\HurtownieDanych\DB_TripOut_dane\dane\odczyt\hotele.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT AtrakcjaDodatkowa 
from 'C:\Users\wronk\projekty\HurtownieDanych\DB_TripOut_dane\dane\odczyt\atrakcje.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT Kwaterowanie 
from 'C:\Users\wronk\projekty\HurtownieDanych\DB_TripOut_dane\dane\odczyt\kwaterowanie.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT Harmonogram 
from 'C:\Users\wronk\projekty\HurtownieDanych\DB_TripOut_dane\dane\odczyt\harmonogram.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);