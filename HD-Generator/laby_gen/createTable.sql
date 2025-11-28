use TripOut				-- HD_biuroPodró¿y 
go 

create table Pilot(
    IdPilota integer primary key, 
    Imie varchar(15) not null, 
    Nazwisko varchar(30) not null, 
    Jezyk varchar(15) not null 
)
go 
 
create table Wycieczka(
    IdWycieczki integer primary key, 
    Kraj varchar(30) not null, 
    Miasto varchar(30) not null, 
    Cena decimal(10,2) not null, 
    Typ varchar(20) not null 
) 
go 

create table Termin(
    IdTerminu integer primary key, 
    DataWyjazdu date not null, 
    DlugoscPobytu integer not null, 
    IloscMiejsc integer not null, 
	IdWycieczki integer foreign key references Wycieczka(IdWycieczki),
)
go 

 
create table Hotel(
    IdHotelu integer primary key, 
    Nazwa varchar(50) not null, 
	Adres varchar(100) not null, 
    StandardHotelu integer not null, 
    ZakresWyzywienia varchar(30) not null, 
    Liczba2osobowych integer not null, 
    Liczba3osobowych integer not null, 
    Liczba4osobowych integer not null, 
    Udogodnienia varchar(20) not null check(Udogodnienia in ('Basen', 'Spa', 'Si³ownia', 'Restauracja')), 
)
go 

 

create table AtrakcjaDodatkowa(
    IdAtrakcjaDodatkowa integer primary key, 
    NazwaAtrakcji varchar(50) not null, 
    Typ varchar(50) not null, 
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
    FK_AtrakcjaDodatkowa integer foreign key references AtrakcjaDodatkowa(IdAtrakcjaDodatkowa), 
    primary key (FK_Wycieczka, FK_AtrakcjaDodatkowa) 
) 
go 

 