create database TripOut				-- HD_biuroPodr�y 
go 

create table Oferta(
    IdOferty integer primary key, 
    IdDaty integer foreign key references Data(IdDaty),
    IdWycieczki integer foreign key references Wycieczka(IdWycieczki),
    IdPilota integer foreign key references Pilot(IdPilota),
    DlugoscPobytu integer not null,
    IloscMiejsc integer not null,
    ZarezerwowaneMiejsca integer not null,
    CenaZaOsobe decimal(10,2) not null,
    Oblozenie integer not null check(Oblozenie between 0 and 100),
    Przychod decimal(10,2) not null
)
go

create table Data(
    IdDaty integer primary key, 
    Data varchar(10) not null,
    Rok integer not null,
    Kwartal integer not null,
    Miesiac varchar(20) not null,
    MiesiacNum integer not null,
    DzienTygodnia varchar(20) not null,
    DzienTygodniaNum integer not null,
    Wakacje bit not null,
    Sezon varchar(10) not null
)
go

create table Hotel(
    IdHotelu integer primary key, 
    BKHotelu integer not null,
    Nazwa varchar(100) not null, 
	Adres varchar(200) not null, 
    Kraj varchar(50) not null, 
    Miasto varchar(50) not null, 
    StandardHotelu integer not null, 
    ZakresWyzywienia varchar(50) not null, 
    LPokoi2os integer not null, 
    LPokoi3os integer not null, 
    LPokoi4os integer not null, 
    UdogodnienieGlowne varchar(50) not null,
    Aktualny bit not null
)
go 

create table Pilot(
    IdPilota integer primary key, 
    ImieNazwisko varchar(100) not null, 
    Jezyk varchar(50) not null 
)
go 
 
create table Wycieczka(
    IdWycieczki integer primary key, 
    Kraj varchar(50) not null, 
    Miasto varchar(50) not null, 
    TypWycieczki varchar(50) not null,
    CenaKat integer not null
) 
go 


create table Atrakcja(
    IdAtrakcji integer primary key, 
    Nazwa varchar(100) not null, 
    Typ varchar(100) not null, 
)
go 


create table Kwaterowanie( 
    FK_Wycieczka integer foreign key references Wycieczka(IdWycieczki), 
    FK_Hotel integer foreign key references Hotel(IdHotelu), 
    primary key (FK_Wycieczka, FK_Hotel) 
)
go 

create table Harmonogram(
    FK_Wycieczka integer foreign key references Wycieczka(IdWycieczki), 
    FK_Atrakcja integer foreign key references Atrakcja(IdAtrakcji), 
    primary key (FK_Wycieczka, FK_Atrakcja)
) 
go 


 


 