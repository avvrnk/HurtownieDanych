#!/usr/bin/env python3
import csv, os, argparse, random, datetime, json
from collections import defaultdict

# ---------- DANE STAlE ---------- 

FIRST_NAMES = [
"Anna","Katarzyna","Maria","Malogorzata","Agnieszka","Barbara","Ewa","Krystyna","Elzbieta","Joanna",
"Zofia","Magdalena","Halina","Teresa","Dorota","Iwona","Beata","Renata","Aleksandra","Natalia",
"Paulina","Monika","Karolina","Julia","Marta","Alicja","Oliwia","Amelia","Marianna","Weronika",
"Patrycja","Izabela","Kinga","Sylwia","Klaudia","Jagoda","Nikola","Adriana","Milena","Dominika",
"Roksana","Laura","Gabriela","Stefania","Antonina","Blanka","Leokadia","Helena","Lidia","Urszula",
"Jan","Piotr","Marek","Tomasz","Pawel","Andrzej","Grzegorz","Krzysztof","Marcin","Lukasz",
"Mateusz","Szymon","Adam","Jakub","Rafal","Dawid","Wojciech","Sebastian","Mariusz","Przemyslaw",
"Arkadiusz","Artur","Bartosz","Cezary","Damian","Dominik","Emil","Filip","Igor","Jacek",
"Kamil","Leszek","Mieczyslaw","Norbert","Olaf","Oskar","Radoslaw","Ryszard","Szczepan","Szymek",
"Teodor","Waldemar","Zygmunt","Zenon","Hubert","Fabian","Eryk","Borys","Maurycy","Constantin",
"Bruno","Dorian","Emanuel","Feliks","Gustaw","Henri","Iwo","Juliusz","Lech","Nikodem","Olgierd",
"Radomir","Witold","Wiktor","Arnold","Cezary","Dorian"
]

SURNAMES = [
"Kowalski","Nowak","Wisniewski","Wojcik","Kowalczyk","Kaminski","Lewandowski","Zielinski","Szymanski","Wozniak",
"Kozlowski","Jankowski","Mazur","Kwiatkowski","Kaczmarek","Piotrowski","Grabowski","Nowicki","Pawlowski","Michalski",
"Olszewski","Nowacki","Majewski","Ostrowski","Malinowski","Jaworski","Wroblewski","Sadowski","Walczak","Baran",
"Rutkowski","Michalak","Bak","Zawadzki","Nawrocki","Duda","Mazurek","Czajkowski","Lis","Sikora",
"Kubiak","Adamski","Gorski","Gajewski","Szulc","Sokolowski","Wasilewski","Lipinski","Wlodarczyk","Nowakowski",
"Markowski","Stepien","Zielinska","Krawczyk","Urban","Tomczak","Krol","Krajewski","Wilk","Orzechowski",
"Wlodarczyk","Blaszczyk","Mika","Kurek","Bednarek","Kubicki","Sikorski","Konecki","Tomaszewski","Kalinowski",
"Jablonski","Rybicki","Nowosielski","Piorkowski","Jaworska","Siwek","Domanski","Mikolajczyk","Stasiak","Kalinowska",
"Leszczynski","Matusiak","Szewczyk","Kruk","Czerwinski","Pawlak","Szczepanski","Kisielewski","Niemczyk","Polak",
"Wilczynski","Sowa","Chmielewski","Biela","Glowacki","Brzezinski","Baczek","Szczepaniak","Kaczor","Borkowski",
"Urbanek","Cichy","Szewczyk","Zaremba","Mikulski","Baron","Wawrzyniak","Gajda","Kubiak","Kurek","Kowal"
]

COUNTRIES_CITIES = {
    "Italy": ["Rome","Milan","Venice"],
    "France": ["Paris","Nice","Lyon"],
    "Spain": ["Barcelona","Madrid","Valencia"],
    "United Kingdom": ["London","Manchester","Edinburgh"],
    "Greece": ["Athens","Thessaloniki"],
    "Portugal": ["Lisbon","Porto"],
    "Croatia": ["Dubrovnik","Split"],
    "Bulgaria": ["Sofia","Burgas"],
    "Germany": ["Berlin","Munich","Hamburg"],
    "Netherlands": ["Amsterdam","Rotterdam"],
    "Belgium": ["Brussels","Antwerp"],
    "Switzerland": ["Zurich","Geneva"],
    "Austria": ["Vienna","Salzburg"],
    "Czech Republic": ["Prague","Ostrava"],
    "Sweden": ["Stockholm","Gothenburg"],
    "Norway": ["Oslo","Bergen"],
    "Denmark": ["Copenhagen","Aarhus"],
    "Turkey": ["Istanbul","Antalya"],
    "Morocco": ["Marrakesh","Casablanca"],
    "Tunisia": ["Tunis","Hammamet"],
    "Egypt": ["Cairo","Hurghada"],
    "USA": ["New York","Los Angeles","Miami"],
    "Canada": ["Toronto","Montreal"],
    "Australia": ["Sydney","Melbourne"],
    "Japan": ["Tokyo","Osaka"],
    "China": ["Beijing","Shanghai"],
    "India": ["Mumbai","Delhi"],
    "Ireland": ["Dublin","Cork"],
    "Iceland": ["Reykjavik","Akureyri"],
    "Poland": ["Warsaw","Krakow","Gdansk"]
}

HEADERS = {
    "piloci": ["IdPilota","Imie","Nazwisko","Jezyk"],
    "hotele": ["IdHotelu","Nazwa","Adres","StandardHotelu","ZakresWyzywienia","LiczbaPokoi2","LiczbaPokoi3","LiczbaPokoi4","Udogodnienie"],
    "wycieczki": ["IdWycieczki","Kraj","Miasto","Cena","Typ","IdPilota"],
    "terminy": ["IdTerminu","DataWyjazdu","DlugoscPobytu","IloscMiejsc","IdWycieczki"],
    "atrakcje": ["IdAtrakcji","Nazwa","Typ"],
    "kwaterowanie": ["IdWycieczki","IdHotelu"],
    "harmonogram": ["IdWycieczki","IdAtrakcji"],
    "rezerwacje": ["Miejscowosc","Termin","Cena","LiczbaOsob"]
}

def ensure_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)

# ---------- GENERATORY ----------
def rnd_name():
    return random.choice(FIRST_NAMES)

def rnd_surname():
    return random.choice(SURNAMES)

def rnd_city_country():
    country = random.choice(list(COUNTRIES_CITIES.keys()))
    city = random.choice(COUNTRIES_CITIES[country])
    return city, country

def generate_pilots(n_pilots, outdir, start_id=1):
    path = os.path.join(outdir, "piloci.csv")
    used_names = set()
    with open(path, "w", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(HEADERS["piloci"])

        for i in range(n_pilots):
            pid = start_id + i
            while True:
                im = rnd_name()
                ns = rnd_surname()
                if (im, ns) not in used_names:
                    used_names.add((im, ns))
                    break
            lang = random.choice(["polski","angielski","wloski","hiszpanski","francuski","niemiecki","rosyjski","arabski","chinski"])
            w.writerow([pid, im, ns, lang])
    return path

def append_pilot(outdir, pid):
    path = os.path.join(outdir, "piloci.csv")
    used_names = set()
    # read existing names to avoid duplicates
    if os.path.exists(path):
        with open(path, newline='', encoding="utf-8") as f:
            r = csv.reader(f, delimiter=';')
            next(r)  # skip header
            for rr in r:
                used_names.add((rr[1], rr[2]))
    while True:
        im = rnd_name()
        ns = rnd_surname()
        if (im, ns) not in used_names:
            used_names.add((im, ns))
            break
    lang = random.choice(["polski","angielski","wloski","hiszpanski","francuski","niemiecki","rosyjski","arabski","chinski"])
    with open(path, "a", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow([pid, im, ns, lang])
    return pid

def generate_hotels(outdir, start_id=1, min_per_city=1, max_per_city=2):
    hotels = []
    hid = start_id
    for country, cities in COUNTRIES_CITIES.items():
        for city in cities:
            num = random.randint(min_per_city, max_per_city)
            for _ in range(num):
                name = f"Hotel_{city}_{hid}"
                addr = f"Ul. {random.choice(['Glowna','Kwiatowa','Przykladowa','Plazowa','Centralna'])} {random.randint(1,300)}"
                standard = random.choices([3,4,5,2,1], weights=[40,30,20,8,2])[0]
                board = random.choice(["sniadania","polpension","pelne wyzywienie","bez wyzywienia"])
                r2 = random.randint(5,200)
                r3 = random.randint(0,50)
                r4 = random.randint(0,30)
                amenities = random.choice([
                                            "Bezplatne Wi-Fi",
                                            "Klimatyzacja w pokojach",
                                            "sniadanie w cenie",
                                            "Calodobowa recepcja",
                                            "Parking (bezplatny lub platny)",
                                            "Silownia / centrum fitness",
                                            "Basen (kryty lub odkryty)",
                                            "Spa i strefa wellness",
                                            "Obsluga pokojowa (room service)",
                                            "Restauracja lub bar hotelowy",
                                            "Transfer z/na lotnisko",
                                            "Przechowalnia bagazu",
                                            "Sejf w pokoju lub w recepcji",
                                            "Telewizor z serwisami streamingowymi",
                                            "Czajnik, kawa i herbata w pokoju",
                                            "Mini bar lub lodowka",
                                            "Udogodnienia dla rodzin",
                                            "Udogodnienia dla osob niepelnosprawnych",
                                            "Centrum biznesowe / sala konferencyjna",
                                            "Usluga pralni i prasowania"])
                hotels.append({
                    "IdHotelu": hid,
                    "Nazwa": name,
                    "Adres": f"{addr}, {city}, {country}",
                    "StandardHotelu": standard,
                    "ZakresWyzywienia": board,
                    "LiczbaPokoi2": r2,
                    "LiczbaPokoi3": r3,
                    "LiczbaPokoi4": r4,
                    "Udogodnienia": amenities,
                    "Miasto": city,
                    "Kraj": country
                })
                hid += 1
    # zapisz do CSV
    path = os.path.join(outdir, "hotele.csv")
    with open(path, "w", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(HEADERS["hotele"])
        for h in hotels:
            w.writerow([h['IdHotelu'], h['Nazwa'], h['Adres'], h['StandardHotelu'],
                        h['ZakresWyzywienia'], h['LiczbaPokoi2'], h['LiczbaPokoi3'], h['LiczbaPokoi4'], h['Udogodnienia']])
    return path, hotels

def generate_trips(n_trips, outdir, start_id=1):
    trips = []
    for i in range(n_trips):
        tid = start_id + i
        city, country = rnd_city_country()
        price = random.randint(40,400)   # cena za dzien za osobe
        typ = random.choice(["objazdowa","wypoczynkowa","city break","tematyczna"])
        trips.append({"IdWycieczki": tid, "Kraj": country, "Miasto": city, "Cena": price, "Typ": typ, "IdPilota": ""})
    path = os.path.join(outdir, "wycieczki.csv")
    with open(path, "w", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(HEADERS["wycieczki"])
        for t in trips:
            w.writerow([t['IdWycieczki'], t['Kraj'], t['Miasto'], t['Cena'], t['Typ'], t['IdPilota']])
    return path, trips

def dates_overlap(a_start, a_end, b_start, b_end):
    return max(a_start, b_start) <= min(a_end, b_end)

def generate_terms(trips, outdir, pilots_ids, start_term_id=1, terms_per_trip=2, append_pilot_fn=None):
    pilot_bookings = {pid: [] for pid in pilots_ids}  # pid -> list of (start,end)
    next_term_id = start_term_id
    # jesli append_pilot_fn nie None, musi zwracac nowe id
    path = os.path.join(outdir, "terminy.csv")
    with open(path, "w", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(HEADERS["terminy"])
        for trip in trips:
            # generate term dates for this trip
            term_ranges = []
            term_rows = []
            temp = []
            for _ in range(terms_per_trip):
                #date_start = datetime.date.today() + datetime.timedelta(days=random.randint(7,365))
                # data rozpoczęcia losowo od 1.01.2020 do 31.12.2025
                date_start = datetime.date(2020,1,1) + datetime.timedelta(days=random.randint(0,2191))
                if date_start in temp:
                    # unikaj duplikatow dat rozpoczęcia dla tej wycieczki
                    while date_start in temp:
                        date_start = datetime.date(2020,1,1) + datetime.timedelta(days=random.randint(0,2191))
                temp.append(date_start)
                length = random.choice([3,5,7,10,14,18,21])
                date_end = date_start + datetime.timedelta(days=length-1)
                seats = random.randint(5,50)
                term_ranges.append((date_start, date_end))
                term_rows.append((next_term_id, date_start.isoformat(), length, seats, trip['IdWycieczki'], date_start, date_end))
                next_term_id += 1
            temp.clear()
            # try znalezc pilota dostępnego dla wszystkich zakresow
            pilot_found = None
            pilot_try_order = pilots_ids.copy()
            random.shuffle(pilot_try_order)
            for pid in pilot_try_order:
                busy = False
                for (ts, te) in term_ranges:
                    for (bs, be) in pilot_bookings.get(pid, []):
                        if dates_overlap(ts, te, bs, be):
                            busy = True
                            break
                    if busy:
                        break
                if not busy:
                    pilot_found = pid
                    break
            if pilot_found is None and append_pilot_fn is not None:
                # utworz nowego pilota i uzyj go
                new_pid = append_pilot_fn()
                pilots_ids.append(new_pid)
                pilot_bookings[new_pid] = []
                pilot_found = new_pid
            # jesli nadal none (brak funkcji append), zostaw puste -> ale sprobujemy z losowym pilotem
            if pilot_found is None:
                pilot_found = random.choice(pilots_ids) if pilots_ids else ""
            # zarejestruj rezerwacje czasu dla pilota
            if pilot_found != "":
                for (ts, te) in term_ranges:
                    pilot_bookings[pilot_found].append((ts, te))
            # uzupelnij w trip
            trip['IdPilota'] = pilot_found
            for tr in term_rows:
                # IdTerminu, DataWyjazdu, DlugoscPobytu, IloscMiejsc, IdWycieczki
                w.writerow([tr[0], tr[1], tr[2], tr[3], tr[4]])
    # po zakonczeniu zapisz zaktualizowane wycieczki (uzupelnione IdPilota)
    trips_path = os.path.join(outdir, "wycieczki.csv")
    with open(trips_path, "w", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(HEADERS["wycieczki"])
        for t in trips:
            w.writerow([t['IdWycieczki'], t['Kraj'], t['Miasto'], t['Cena'], t['Typ'], t['IdPilota']])
    return path, trips

def generate_attractions(n_atr, outdir, start_id=1):
    path = os.path.join(outdir, "atrakcje.csv")
    with open(path, "w", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(HEADERS["atrakcje"])
        for i in range(n_atr):
            aid = start_id + i
            name = f"Atrakcja_{aid}"
            typ = random.choice(["wycieczka","wystawa","degustacja","koncert","zwiedzanie","pokaz","warsztaty","inne"])
            w.writerow([aid, name, typ])
    return path

def generate_kwaterowanie(trips, hotels_info, outdir):
    city_hotels = defaultdict(list)
    for h in hotels_info:
        city_hotels[h['Miasto']].append(h['IdHotelu'])
    path = os.path.join(outdir, "kwaterowanie.csv")
    with open(path, "w", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(HEADERS["kwaterowanie"])
        for t in trips:
            city = t['Miasto']
            available = city_hotels.get(city, [])
            # przypisz 1 hotel z tego miasta
            # if available:
            #     hid = random.choice(available)
            #     w.writerow([t['IdWycieczki'], hid])


            if not available:
                hotel_choice = [random.choice([h['IdHotelu'] for h in hotels_info])]
            else:
                k = min(len(available), random.randint(1, min(3, len(available))))
                hotel_choice = random.sample(available, k=k)
            for hid in hotel_choice:
                w.writerow([t['IdWycieczki'], hid])
    return path

def generate_harmonogram(trips_ids, attractions_ids, outdir):
    path = os.path.join(outdir, "harmonogram.csv")
    with open(path, "w", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(HEADERS["harmonogram"])
        for t in trips_ids:
            # przypisz 1 atrakcji na wycieczkę
            # a = random.choice(attractions_ids)
            # w.writerow([t, a])
            k = random.randint(0, 3)
            for a in random.sample(attractions_ids, k=min(k, len(attractions_ids))):
               w.writerow([t, a])
    return path

def read_terms_rows(terminy_csv):
    rows = []
    with open(terminy_csv, newline='', encoding="utf-8") as f:
        r = csv.DictReader(f, delimiter=';')
        for rr in r:
            # IdTerminu, IdWycieczki, DataWyjazdu, DlugoscPobytu, IloscMiejsc
            rows.append((int(rr['IdTerminu']), int(rr['IdWycieczki']), rr['DataWyjazdu'], int(rr['DlugoscPobytu']), int(rr['IloscMiejsc'])))
    return rows

def generate_rezerwacje_csv_stream(terms_rows, trip_city_map, trip_price_map, outpath, seed_offset=0):
    random.seed(42 + seed_offset)
    with open(outpath, "w", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(HEADERS["rezerwacje"])
        N = len(terms_rows)
        for i in range(N):
            term = terms_rows[i]
            trip_id = term[1]
            city = trip_city_map.get(trip_id, "Nieznane")
            price = trip_price_map.get(trip_id, random.randint(200, 3000))
            seats_available = int(term[4])
            booked = random.randint(1, seats_available)

            #booked = max(1, int(random.gauss(seats_available*0.5, max(1, seats_available*0.2))))
            #booked = min(seats_available, max(0, booked))
            w.writerow([city, term[2], price, booked])
    return outpath

def main():
    outdir = os.environ.get("OUTDIR", "XDDDDD")
    pilots = int(os.environ.get("PILOTS", "50"))
    trips = int(os.environ.get("TRIPS", "1000"))
    random.seed(12345)
    ensure_dir(outdir)

    # 1) Piloci
    pilots_csv = generate_pilots(pilots, outdir, start_id=1)
    pilots_ids = list(range(1, pilots+1))
    next_pilot_id = pilots + 1

    def append_pilot_fn():
        nonlocal next_pilot_id
        pid = next_pilot_id
        append_pilot(outdir, pid)
        next_pilot_id += 1
        return pid

    # 2) Hotele (przypisane do miast)
    hotels_csv, hotels_info = generate_hotels(outdir, start_id=1, min_per_city=2, max_per_city=5)
    hotels_ids = [h['IdHotelu'] for h in hotels_info]

    # 3) Wycieczki (bez pilota na razie)
    trips_csv, trips_list = generate_trips(trips, outdir, start_id=1)
    trips_ids = [t['IdWycieczki'] for t in trips_list]

    # 4) Terminy - w trakcie ich tworzenia przypisujemy pilota, dbajac o konflikty
    termy_csv, trips_list = generate_terms(trips_list, outdir, pilots_ids, start_term_id=1, terms_per_trip=3, append_pilot_fn=append_pilot_fn)

    # 5) Atrakcje
    #atrakcje_csv = generate_attractions(128, outdir, start_id=1)
    attractions_ids = list(range(1, 125+1))

    # 6) Kwaterowanie: przypiszemy tylko hotele z tego samego miasta co wycieczka
    kw_csv = generate_kwaterowanie(trips_list, hotels_info, outdir)

    # 7) Harmonogram
    harm_csv = generate_harmonogram(trips_ids, attractions_ids, outdir)

    # 8) Rezerwacje: odczytamy terminy i wygenerujemy fakty
    terms_rows = read_terms_rows(termy_csv)
    trip_city_map = {t['IdWycieczki']: t['Miasto'] for t in trips_list}
    trip_price_map = {t['IdWycieczki']: t['Cena'] for t in trips_list}
    rezerwacje_t1 = os.path.join(outdir, "rezerwacje.csv")
    generate_rezerwacje_csv_stream(terms_rows, trip_city_map, trip_price_map, rezerwacje_t1, seed_offset=0)

    print("Generated files under:", os.path.abspath(outdir))
    print("Pilots total (including auto-added if any):", next_pilot_id - 1)

if __name__ == "__main__":
    main()
