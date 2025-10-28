#!/usr/bin/env python3
"""
generator_tripout.py
Generuje źródła danych (CSV) i skrypty SQL (CREATE TABLE + BULK INSERT) dla zadania DW_Instruction_2.
Zapisuje snapshoty T1 i T2. Skalowalny do ~1_000_000 faktów (używaj streamingowego zapisu).
"""
import csv, os, argparse, random, datetime, json

def rnd_name():
    return random.choice(["Jan","Anna","Piotr","Katarzyna","Marek","Agnieszka","Tomasz","Ewa"])
def rnd_surname():
    return random.choice(["Kowalski","Nowak","Wiśniewski","Wójcik","Kaczmarek","Mazur"])
def rnd_city_country():
    pairs = [
        ("Rzym","Włochy"),("Paryż","Francja"),("Barcelona","Hiszpania"),
        ("Londyn","Wielka Brytania"),("Ateny","Grecja"),("Lizbona","Portugalia"),
        ("Dubrownik","Chorwacja"),("Sofia","Bułgaria")
    ]
    return random.choice(pairs)
def ensure_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)
HEADERS = {
    "pilots": ["IdPilota","Imie","Nazwisko","Jezyk"],
    "hotels": ["IdHotelu","Nazwa","Adres","StandardHotelu","ZakresWyzywienia","LiczbaPokoi2","LiczbaPokoi3","LiczbaPokoi4","Udogodnienia"],
    "wycieczki": ["IdWycieczki","Kraj","Miasto","Cena","Typ","IdPilota"],
    "terminy": ["IdTerminu","DataWyjazdu","DlugoscPobytu","IloscMiejsc","IdWycieczki"],
    "atrakcje": ["IdAtrakcji","Nazwa","Typ"],
    "kwaterowanie": ["IdWycieczki","IdHotelu"],
    "harmonogram": ["IdWycieczki","IdAtrakcji"],
    "rezerwacje": ["Miejscowosc","Termin","Cena","LiczbaOsob"]
}
# CREATE_TABLES_SQL = r\"\"\"-- CREATE TABLE scripts for TripOut source (MS SQL Server)
# CREATE TABLE Pilot (
#   IdPilota INT PRIMARY KEY,
#   Imie NVARCHAR(50),
#   Nazwisko NVARCHAR(50),
#   Jezyk NVARCHAR(50)
# );
# CREATE TABLE Hotel (
#   IdHotelu INT PRIMARY KEY,
#   Nazwa NVARCHAR(100),
#   Adres NVARCHAR(255),
#   StandardHotelu INT,
#   ZakresWyzywienia NVARCHAR(100),
#   LiczbaPokoi2 INT,
#   LiczbaPokoi3 INT,
#   LiczbaPokoi4 INT,
#   Udogodnienia NVARCHAR(255)
# );
# CREATE TABLE Wycieczka (
#   IdWycieczki INT PRIMARY KEY,
#   Kraj NVARCHAR(50),
#   Miasto NVARCHAR(50),
#   Cena DECIMAL(10,2),
#   Typ NVARCHAR(50),
#   IdPilota INT REFERENCES Pilot(IdPilota)
# );
# CREATE TABLE Termin (
#   IdTerminu INT PRIMARY KEY,
#   IdWycieczki INT REFERENCES Wycieczka(IdWycieczki),
#   DataWyjazdu DATE,
#   DlugoscPobytu INT,
#   IloscMiejsc INT
# );
# CREATE TABLE AtrakcjaDodatkowa (
#   IdAtrakcji INT PRIMARY KEY,
#   Nazwa NVARCHAR(100),
#   Typ NVARCHAR(50)
# );
# CREATE TABLE Kwaterowanie (
#   IdWycieczki INT REFERENCES Wycieczka(IdWycieczki),
#   IdHotelu INT REFERENCES Hotel(IdHotelu),
#   PRIMARY KEY (IdWycieczki, IdHotelu)
# );
# CREATE TABLE Harmonogram (
#   IdWycieczki INT REFERENCES Wycieczka(IdWycieczka),
#   IdAtrakcji INT REFERENCES AtrakcjaDodatkowa(IdAtrakcji),
#   PRIMARY KEY (IdWycieczki, IdAtrakcji)
# );
# \"\"\"
# BULK_INSERT_TEMPLATE = \"\"\"BULK INSERT {table}
# FROM '{filepath}'
# WITH (
#   FIELDTERMINATOR = ';',
#   ROWTERMINATOR = '\\n',
#   FIRSTROW = 2,
#   CODEPAGE = '65001'
# );
# \"\"\"
def generate_pilots(n_pilots, outdir, start_id=1):
    path = os.path.join(outdir, "pilots.csv")
    with open(path, "w", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(HEADERS["pilots"])
        for i in range(n_pilots):
            pid = start_id + i
            im = rnd_name()
            ns = rnd_surname()
            lang = random.choice(["polski","angielski","włoski","hiszpański","francuski","niemiecki"])
            w.writerow([pid, im, ns, lang])
    return path
def generate_hotels(n_hotels, outdir, start_id=1):
    path = os.path.join(outdir, "hotels.csv")
    with open(path, "w", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(HEADERS["hotels"])
        for i in range(n_hotels):
            hid = start_id + i
            name = f"Hotel_{hid}"
            addr = f"Ul. Przykładowa {random.randint(1,200)}, {random.choice(['MiastoA','MiastoB','MiastoC'])}"
            standard = random.choices([3,4,5,2,1], weights=[40,30,20,8,2])[0]
            board = random.choice(["śniadania","półpension","pełne wyżywienie","bez wyżywienia"])
            r2 = random.randint(5,100)
            r3 = random.randint(0,30)
            r4 = random.randint(0,15)
            amenities = random.choice(["basen;wifi","spa;basen","wifi;parking","brak"])
            w.writerow([hid, name, addr, standard, board, r2, r3, r4, amenities])
    return path
def generate_trips(n_trips, pilots_ids, outdir, start_id=1):
    path = os.path.join(outdir, "wycieczki.csv")
    with open(path, "w", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(HEADERS["wycieczki"])
        for i in range(n_trips):
            tid = start_id + i
            city,country = rnd_city_country()
            price = random.randint(300,3500)
            typ = random.choice(["objazdowa","wypoczynkowa","city break","tematyczna"])
            pilot = random.choice(pilots_ids)
            w.writerow([tid, country, city, price, typ, pilot])
    return path
def generate_terms(trips_ids, outdir, start_id=1, terms_per_trip=3):
    path = os.path.join(outdir, "terminy.csv")
    with open(path, "w", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(HEADERS["terminy"])
        tid = start_id
        for t in trips_ids:
            for _ in range(terms_per_trip):
                date = datetime.date.today() + datetime.timedelta(days=random.randint(7,365))
                lenp = random.choice([3,5,7,10,14,18,21])
                seats = random.randint(5,50)
                w.writerow([tid, date.isoformat(), lenp, seats, t])
                tid += 1
    return path
def generate_attractions(n_atr, outdir, start_id=1):
    path = os.path.join(outdir, "atrakcje.csv")
    with open(path, "w", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(HEADERS["atrakcje"])
        for i in range(n_atr):
            aid = start_id + i
            name = f"Atrakcja_{aid}"
            typ = random.choice(["wycieczka","wystawa","degustacja","koncert"])
            w.writerow([aid, name, typ])
    return path
def generate_kwaterowanie(trips_ids, hotels_ids, outdir):
    path = os.path.join(outdir, "kwaterowanie.csv")
    with open(path, "w", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(HEADERS["kwaterowanie"])
        for t in trips_ids:
            for h in random.sample(hotels_ids, k=min(len(hotels_ids), random.randint(1,3))):
                w.writerow([t, h])
    return path
def generate_harmonogram(trips_ids, attractions_ids, outdir):
    path = os.path.join(outdir, "harmonogram.csv")
    with open(path, "w", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(HEADERS["harmonogram"])
        for t in trips_ids:
            for a in random.sample(attractions_ids, k=min(len(attractions_ids), random.randint(0,3))):
                w.writerow([t, a])
    return path
def generate_rezerwacje_csv_stream(n_facts, terms_rows, outpath, seed_offset=0):
    random.seed(42 + seed_offset)
    with open(outpath, "w", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(HEADERS["rezerwacje"])
        N = len(terms_rows)
        for i in range(n_facts):
            term = terms_rows[random.randint(0, N-1)]
            seats_available = int(term[4])
            booked = max(1, int(random.gauss(seats_available*0.5, max(1, seats_available*0.2))))
            booked = min(seats_available, max(0, booked))
            price = random.randint(200, 3000)
            w.writerow([term[2], term[0], price, booked])
    return outpath
def read_terms_rows(terminy_csv):
    rows = []
    with open(terminy_csv, newline='', encoding="utf-8") as f:
        r = csv.DictReader(f, delimiter=';')
        for rr in r:
            rows.append((int(rr['IdTerminu']), int(rr['IdWycieczki']), rr['DataWyjazdu'], int(rr['DlugoscPobytu']), int(rr['IloscMiejsc'])))
    return rows
def main():
    outdir = os.environ.get("OUTDIR", "out_data")
    facts = int(os.environ.get("FACTS", "1000000"))
    pilots = int(os.environ.get("PILOTS", "5"))
    hotels = int(os.environ.get("HOTELS", "10"))
    trips = int(os.environ.get("TRIPS", "50"))
    random.seed(12345)
    ensure_dir(outdir)
    pilots_csv = generate_pilots(pilots, outdir, start_id=1)
    hotels_csv = generate_hotels(hotels, outdir, start_id=1)
    pilots_ids = list(range(1, pilots+1))
    trips_csv = generate_trips(trips, pilots_ids, outdir, start_id=1)
    trips_ids = list(range(1, trips+1))
    hotels_ids = list(range(1, hotels+1))
    termy_csv = generate_terms(trips_ids, outdir, start_id=1, terms_per_trip=2)
    atrakcje_csv = generate_attractions(20, outdir, start_id=1)
    attractions_ids = list(range(1, 20+1))
    kw_csv = generate_kwaterowanie(trips_ids, hotels_ids, outdir)
    harm_csv = generate_harmonogram(trips_ids, attractions_ids, outdir)
    terms_rows = read_terms_rows(termy_csv)
    rezerwacje_t1 = os.path.join(outdir, "rezerwacje_T1.csv")
    generate_rezerwacje_csv_stream(facts, terms_rows, rezerwacje_t1, seed_offset=0)
    extra = max(1, int(facts * 0.2))
    rezerwacje_t2 = os.path.join(outdir, "rezerwacje_T2.csv")
    generate_rezerwacje_csv_stream(facts + extra, terms_rows, rezerwacje_t2, seed_offset=1)
    hotels_t2 = os.path.join(outdir, "hotels_T2.csv")
    with open(hotels_csv, newline='', encoding="utf-8") as fin, open(hotels_t2, "w", newline='', encoding="utf-8") as fout:
        r = csv.DictReader(fin, delimiter=';')
        w = csv.writer(fout, delimiter=';')
        w.writerow(HEADERS["hotels"])
        for rr in r:
            if int(rr['IdHotelu']) == 1:
                rr['StandardHotelu'] = str(min(5, int(rr['StandardHotelu']) + 1))
                rr['Nazwa'] = rr['Nazwa'] + "_v2"
            w.writerow([rr[h] for h in HEADERS['hotels']])
    # create_sql_path = os.path.join(outdir, "create_tables.sql")
    # with open(create_sql_path, "w", encoding="utf-8") as f:
    #     f.write(CREATE_TABLES_SQL)
    # bulk_t1 = os.path.join(outdir, "bulk_load_T1.sql")
    # with open(bulk_t1, "w", encoding="utf-8") as f:
    #     f.write("-- Adjust paths before executing on SQL Server\n")
    #     for name,file in [("Pilot",pilots_csv),("Hotel",hotels_csv),("Wycieczka",trips_csv),("Termin",termy_csv),
    #                       ("AtrakcjaDodatkowa",atrakcje_csv),("Kwaterowanie",kw_csv),("Harmonogram",harm_csv)]:
    #         f.write(BULK_INSERT_TEMPLATE.format(table=name, filepath=os.path.abspath(file)))
    #     f.write(BULK_INSERT_TEMPLATE.format(table="Rezerwacje", filepath=os.path.abspath(rezerwacje_t1)))
    # bulk_t2 = os.path.join(outdir, "bulk_load_T2.sql")
    # with open(bulk_t2, "w", encoding="utf-8") as f:
    #     f.write("-- For T2 (includes changed hotels_T2.csv and expanded rezerwacje_T2.csv)\n")
    #     f.write(BULK_INSERT_TEMPLATE.format(table="Hotel", filepath=os.path.abspath(hotels_t2)))
    #     f.write(BULK_INSERT_TEMPLATE.format(table="Rezerwacje", filepath=os.path.abspath(rezerwacje_t2)))
    print("Generated files under:", os.path.abspath(outdir))
if __name__ == "__main__":
    main()
