use TripOut				-- HD_biuroPodró¿y
go 

BULK INSERT Pilot 
from 'C:\Users\wronk\projekty\HurtownieDanych\HD-Generator\Generator\dane_docelowe\pilots.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT Wycieczka 
from 'C:\Users\wronk\projekty\HurtownieDanych\HD-Generator\Generator\dane_docelowe\wycieczki.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT Termin 
from 'C:\Users\wronk\projekty\HurtownieDanych\HD-Generator\Generator\dane_docelowe\terminy.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT Hotel 
from 'C:\Users\wronk\projekty\HurtownieDanych\HD-Generator\Generator\dane_docelowe\hotels.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT AtrakcjaDodatkowa 
from 'C:\Users\wronk\projekty\HurtownieDanych\HD-Generator\Generator\dane_docelowe\atrakcje.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT Kwaterowanie 
from 'C:\Users\wronk\projekty\HurtownieDanych\HD-Generator\Generator\dane_docelowe\kwaterowanie.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT Harmonogram 
from 'C:\Users\wronk\projekty\HurtownieDanych\HD-Generator\Generator\dane_docelowe\harmonogram.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);
