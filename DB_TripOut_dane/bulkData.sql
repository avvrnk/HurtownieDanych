use TripOutDB				-- HD_biuroPodró¿y
go 

BULK INSERT Pilot 
from 'C:\Users\wronk\projekty\HurtownieDanych\DB_TripOut_dane\dane\piloci.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT Wycieczka 
from 'C:\Users\wronk\projekty\HurtownieDanych\DB_TripOut_dane\dane\wycieczki.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT Termin 
from 'C:\Users\wronk\projekty\HurtownieDanych\DB_TripOut_dane\dane\terminy.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT Hotel 
from 'C:\Users\wronk\projekty\HurtownieDanych\DB_TripOut_dane\dane\hotele.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT AtrakcjaDodatkowa 
from 'C:\Users\wronk\projekty\HurtownieDanych\DB_TripOut_dane\dane\atrakcje.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT Kwaterowanie 
from 'C:\Users\wronk\projekty\HurtownieDanych\DB_TripOut_dane\dane\kwaterowanie.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT Harmonogram 
from 'C:\Users\wronk\projekty\HurtownieDanych\DB_TripOut_dane\dane\harmonogram.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);
