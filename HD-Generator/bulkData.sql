use TripOut				-- HD_biuroPodró¿y
go 

BULK INSERT Pilot 
from 'C:\Users\Agata\projekty\HD-Generator\out_data\pilots.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT Wycieczka 
from 'C:\Users\Agata\projekty\HD-Generator\out_data\wycieczki.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT Termin 
from 'C:\Users\Agata\projekty\HD-Generator\out_data\terminy.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT Hotel 
from 'C:\Users\Agata\projekty\HD-Generator\out_data\hotels.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT AtrakcjaDodatkowa 
from 'C:\Users\Agata\projekty\HD-Generator\out_data\atrakcje.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT Kwaterowanie 
from 'C:\Users\Agata\projekty\HD-Generator\out_data\kwaterowanie.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);

BULK INSERT Harmonogram 
from 'C:\Users\Agata\projekty\HD-Generator\out_data\harmonogram.csv'
WITH (
	FIELDTERMINATOR=';',
	ROWTERMINATOR = '\n', 
	FIRSTROW = 2, 
	CODEPAGE = 65001
	);
