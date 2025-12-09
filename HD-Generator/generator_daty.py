import datetime
import csv

miesiace = {
    1: "Styczen", 2: "Luty", 3: "Marzec", 4: "Kwiecien",
    5: "Maj", 6: "Czerwiec", 7: "Lipiec", 8: "Sierpien",
    9: "Wrzesien", 10: "Pazdziernik", 11: "Listopad", 12: "Grudzien"
}

dni_tyg = {
    1: "Poniedzialek", 2: "Wtorek", 3: "Sroda", 4: "Czwartek",
    5: "Piatek", 6: "Sobota", 7: "Niedziela"
}

def kwartal(m):
    return (m - 1) // 3 + 1

def sezon(m):
    if m in (12, 1, 2):
        return "Zima"
    if m in (3, 4, 5):
        return "Wiosna"
    if m in (6, 7, 8):
        return "Lato"
    return "Jesien"

start = datetime.date(2020, 1, 1)
end   = datetime.date(2025, 12, 31)

current = start
id_counter = 1

with open("dane\daty.csv", "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=';')

    while current <= end:
        rok = current.year
        mies = current.month
        dzien = current.day

        data_str = current.strftime("%Y-%m-%d")
        kwart = kwartal(mies)

        dzien_tyg_num = current.weekday() + 1
        dzien_tyg_txt = dni_tyg[dzien_tyg_num]

        wakacje = 1 if mies in (7, 8) else 0
        sezon_txt = sezon(mies)

        writer.writerow([
            id_counter, data_str, rok, kwart,
            miesiace[mies], mies, dzien,
            dzien_tyg_txt, dzien_tyg_num,
            wakacje, sezon_txt
        ])

        current += datetime.timedelta(days=1)
        id_counter += 1

print("Plik daty.csv zapisany!")
