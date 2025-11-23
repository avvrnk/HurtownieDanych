#!/usr/bin/env python3
import csv, os, argparse, random, datetime, json
from collections import defaultdict

FIRST_NAMES = [
"Anna","Katarzyna","Maria","Małgorzata","Agnieszka","Barbara","Ewa","Krystyna","Elżbieta","Joanna",
"Zofia","Magdalena","Halina","Teresa","Dorota","Iwona","Beata","Renata","Aleksandra","Natalia",
"Paulina","Monika","Karolina","Julia","Marta","Alicja","Oliwia","Amelia","Marianna","Weronika",
"Patrycja","Izabela","Kinga","Sylwia","Klaudia","Jagoda","Nikola","Adriana","Milena","Dominika",
"Roksana","Laura","Gabriela","Stefania","Antonina","Blanka","Leokadia","Helena","Lidia","Urszula",
"Jan","Piotr","Marek","Tomasz","Paweł","Andrzej","Grzegorz","Krzysztof","Marcin","Łukasz",
"Mateusz","Szymon","Adam","Jakub","Rafał","Dawid","Wojciech","Sebastian","Mariusz","Przemysław",
"Arkadiusz","Artur","Bartosz","Cezary","Damian","Dominik","Emil","Filip","Igor","Jacek",
"Kamil","Leszek","Mieczysław","Norbert","Olaf","Oskar","Radosław","Ryszard","Szczepan","Szymek",
"Teodor","Waldemar","Zygmunt","Zenon","Hubert","Fabian","Eryk","Borys","Maurycy","Constantin",
"Bruno","Dorian","Emanuel","Feliks","Gustaw","Henri","Iwo","Juliusz","Lech","Nikodem","Olgierd",
"Radomir","Witold","Wiktor","Arnold","Cezary","Dorian"
]

SURNAMES = [
"Kowalski","Nowak","Wiśniewski","Wójcik","Kowalczyk","Kamiński","Lewandowski","Zieliński","Szymański","Woźniak",
"Kozłowski","Jankowski","Mazur","Kwiatkowski","Kaczmarek","Piotrowski","Grabowski","Nowicki","Pawłowski","Michalski",
"Olszewski","Nowacki","Majewski","Ostrowski","Malinowski","Jaworski","Wróblewski","Sadowski","Walczak","Baran",
"Rutkowski","Michalak","Bąk","Zawadzki","Nawrocki","Duda","Mazurek","Czajkowski","Lis","Sikora",
"Kubiak","Adamski","Górski","Gajewski","Szulc","Sokołowski","Wasilewski","Lipinski","Włodarczyk","Nowakowski",
"Markowski","Stępień","Zielińska","Krawczyk","Urban","Tomczak","Król","Krajewski","Wilk","Orzechowski",
"Włodarczyk","Błaszczyk","Mika","Kurek","Bednarek","Kubicki","Sikorski","Konecki","Tomaszewski","Kalinowski",
"Jabłoński","Rybicki","Nowosielski","Piórkowski","Jaworska","Siwek","Domański","Mikołajczyk","Stasiak","Kalinowska",
"Leszczyński","Matusiak","Szewczyk","Kruk","Czerwiński","Pawlak","Szczepański","Kisielewski","Niemczyk","Polak",
"Wilczyński","Sowa","Chmielewski","Biela","Głowacki","Brzeziński","Bączek","Szczepaniak","Kaczor","Borkowski",
"Urbanek","Cichy","Szewczyk","Zaremba","Mikulski","Baron","Wawrzyniak","Gajda","Kubiak","Kurek","Kowal"
]

# ~30 krajów z 2-3 miastami każdy (przykładowe)
COUNTRIES_CITIES = {
    "Włochy": ["Rzym","Mediolan","Wenecja"],
    "Francja": ["Paryż","Nicea","Lyon"],
    "Hiszpania": ["Barcelona","Madryt","Walencja"],
    "Wielka Brytania": ["Londyn","Manchester","Edynburg"],
    "Grecja": ["Ateny","Saloniki"],
    "Portugalia": ["Lizbona","Porto"],
    "Chorwacja": ["Dubrownik","Split"],
    "Bułgaria": ["Sofia","Burgas"],
    "Niemcy": ["Berlin","Monachium","Hamburg"],
    "Holandia": ["Amsterdam","Rotterdam"],
    "Belgia": ["Bruksela","Antwerpia"],
    "Szwajcaria": ["Zurych","Genewa"],
    "Austria": ["Wiedeń","Salzburg"],
    "Czechy": ["Praga","Ostrawa"],
    "Szwecja": ["Sztokholm","Gothenburg"],
    "Norwegia": ["Oslo","Bergen"],
    "Dania": ["Kopenhaga","Aarhus"],
    "Turcja": ["Stambuł","Antalya"],
    "Maroko": ["Marrakesz","Casablanca"],
    "Tunezja": ["Tunis","Hammamet"],
    "Egipt": ["Kair","Hurghada"],
    "USA": ["Nowy Jork","Los Angeles","Miami"],
    "Kanada": ["Toronto","Montreal"],
    "Australia": ["Sydney","Melbourne"],
    "Japonia": ["Tokio","Osaka"],
    "Chiny": ["Pekin","Szanghaj"],
    "Indie": ["Mumbaj","Delhi"],
    "Irlandia": ["Dublin","Cork"],
    "Islandia": ["Reykjavik","Akureyri"],
    "Polska": ["Warszawa","Kraków","Gdańsk"]
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
            lang = random.choice(["polski","angielski","włoski","hiszpański","francuski","niemiecki","rosyjski","arabski","chiński"])
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
    lang = random.choice(["polski","angielski","włoski","hiszpański","francuski","niemiecki","rosyjski","arabski","chiński"])
    with open(path, "a", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow([pid, im, ns, lang])
    return pid

def generate_hotels(outdir, start_id=1, min_per_city=1, max_per_city=3):
    hotels = []
    hid = start_id
    for country, cities in COUNTRIES_CITIES.items():
        for city in cities:
            num = random.randint(min_per_city, max_per_city)
            for _ in range(num):
                name = f"Hotel_{city}_{hid}"
                addr = f"Ul. {random.choice(['Główna','Kwiatowa','Przykładowa','Plażowa','Centralna'])} {random.randint(1,300)}, {city}"
                standard = random.choices([3,4,5,2,1], weights=[40,30,20,8,2])[0]
                board = random.choice(["śniadania","półpension","pełne wyżywienie","bez wyżywienia"])
                r2 = random.randint(5,200)
                r3 = random.randint(0,50)
                r4 = random.randint(0,30)
                amenities = random.choice([
                                            "Bezpłatne Wi-Fi",
                                            "Klimatyzacja w pokojach",
                                            "Śniadanie w cenie",
                                            "Całodobowa recepcja",
                                            "Parking (bezpłatny lub płatny)",
                                            "Siłownia / centrum fitness",
                                            "Basen (kryty lub odkryty)",
                                            "Spa i strefa wellness",
                                            "Obsługa pokojowa (room service)",
                                            "Restauracja lub bar hotelowy",
                                            "Transfer z/na lotnisko",
                                            "Przechowalnia bagażu",
                                            "Sejf w pokoju lub w recepcji",
                                            "Telewizor z serwisami streamingowymi",
                                            "Czajnik, kawa i herbata w pokoju",
                                            "Mini bar lub lodówka",
                                            "Udogodnienia dla rodzin",
                                            "Udogodnienia dla osób niepełnosprawnych",
                                            "Centrum biznesowe / sala konferencyjna",
                                            "Usługa pralni i prasowania"])
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
        price = random.randint(300,2500)
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

def generate_terms(trips, outdir, pilots_ids, start_term_id=1, terms_per_trip=3, append_pilot_fn=None):
    pilot_bookings = {pid: [] for pid in pilots_ids}  # pid -> list of (start,end)
    next_term_id = start_term_id
    # jeśli append_pilot_fn nie None, musi zwracać nowe id
    path = os.path.join(outdir, "terminy.csv")
    with open(path, "w", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(HEADERS["terminy"])
        for trip in trips:
            # generate term dates for this trip
            term_ranges = []
            term_rows = []
            for _ in range(terms_per_trip):
                date_start = datetime.date.today() + datetime.timedelta(days=random.randint(7,365))
                length = random.choice([3,5,7,10,14,18,21])
                date_end = date_start + datetime.timedelta(days=length-1)
                seats = random.randint(5,50)
                term_ranges.append((date_start, date_end))
                term_rows.append((next_term_id, date_start.isoformat(), length, seats, trip['IdWycieczki'], date_start, date_end))
                next_term_id += 1
            # try znaleźć pilota dostępnego dla wszystkich zakresów
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
                # utwórz nowego pilota i użyj go
                new_pid = append_pilot_fn()
                pilots_ids.append(new_pid)
                pilot_bookings[new_pid] = []
                pilot_found = new_pid
            # jeśli nadal none (brak funkcji append), zostaw puste -> ale spróbujemy z losowym pilotem
            if pilot_found is None:
                pilot_found = random.choice(pilots_ids) if pilots_ids else ""
            # zarejestruj rezerwacje czasu dla pilota
            if pilot_found != "":
                for (ts, te) in term_ranges:
                    pilot_bookings[pilot_found].append((ts, te))
            # uzupełnij w trip
            trip['IdPilota'] = pilot_found
            for tr in term_rows:
                # IdTerminu, DataWyjazdu, DlugoscPobytu, IloscMiejsc, IdWycieczki
                w.writerow([tr[0], tr[1], tr[2], tr[3], tr[4]])
    # po zakończeniu zapisz zaktualizowane wycieczki (uzupełnione IdPilota)
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

def generate_rezerwacje_csv_stream(n_facts, terms_rows, trip_city_map, outpath, seed_offset=0):
    random.seed(42 + seed_offset)
    with open(outpath, "w", newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(HEADERS["rezerwacje"])
        N = len(terms_rows)
        for i in range(n_facts):
            term = terms_rows[random.randint(0, N-1)]
            trip_id = term[1]
            city = trip_city_map.get(trip_id, "Nieznane")
            seats_available = int(term[4])
            booked = max(1, int(random.gauss(seats_available*0.5, max(1, seats_available*0.2))))
            booked = min(seats_available, max(0, booked))
            price = random.randint(200, 3000)
            w.writerow([city, term[2], price, booked])
    return outpath

def main():
    outdir = os.environ.get("OUTDIR", "out_data")
    facts = int(os.environ.get("FACTS", "1000000"))
    pilots = int(os.environ.get("PILOTS", "500"))
    trips = int(os.environ.get("TRIPS", "100000"))
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

    # 4) Terminy - w trakcie ich tworzenia przypisujemy pilota, dbając o konflikty
    termy_csv, trips_list = generate_terms(trips_list, outdir, pilots_ids, start_term_id=1, terms_per_trip=3, append_pilot_fn=append_pilot_fn)

    # 5) Atrakcje
    atrakcje_csv = generate_attractions(128, outdir, start_id=1)
    attractions_ids = list(range(1, 128+1))

    # 6) Kwaterowanie: przypiszemy tylko hotele z tego samego miasta co wycieczka
    kw_csv = generate_kwaterowanie(trips_list, hotels_info, outdir)

    # 7) Harmonogram
    harm_csv = generate_harmonogram(trips_ids, attractions_ids, outdir)

    # 8) Rezerwacje: odczytamy terminy i wygenerujemy fakty
    terms_rows = read_terms_rows(termy_csv)
    trip_city_map = {t['IdWycieczki']: t['Miasto'] for t in trips_list}
    rezerwacje_t1 = os.path.join(outdir, "rezerwacje.csv")
    generate_rezerwacje_csv_stream(facts, terms_rows, trip_city_map ,rezerwacje_t1, seed_offset=0)

    print("Generated files under:", os.path.abspath(outdir))
    print("Pilots total (including auto-added if any):", next_pilot_id - 1)

if __name__ == "__main__":
    main()
