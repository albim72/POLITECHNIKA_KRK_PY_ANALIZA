print("Kolekcje Pythona")
#kolekcja - lista
liczby = [6,8,13,45,6,9,3,0,123,13,13]

print(liczby)
print(liczby[0])
print(liczby[2:5])

liczby.append(6667)
print(liczby)
liczby.insert(3,543)
print(liczby)
liczbyX = liczby[:]
liczbyX.sort()
print(liczbyX)
print(liczby)

#tuple - krotka
miasta = ("Kraków","Lublin","Warszawa","Katowice","Wrocław","Kraków")
print(miasta)
print(miasta[1])
print(miasta[-1 ])
print(miasta.index("Katowice"))
print(miasta.count("Kraków"))

#zbiór - set
kolory = {"zielony","czerwony","biały","czarny","różowy","niebieski","zielony"}
print(kolory)
print(kolory)
print(kolory)
kolory.add("fioletowy")
print(kolory)


print(liczby)
liczby = set(liczby)
liczby = list(liczby)
print(liczby)

#słownik
osoba = {
    "imię":"Jan",
    "nazwisko":"Nowak",
    "miasto":"Toruń",
    "wiek":45,
    222:657768,
    333:True
}
print(osoba)
print(osoba["miasto"])
print(osoba[333])

osoba["kolor_oczu"] = "niebieskie"
print(osoba)

print(osoba.keys())
print(osoba.values())
print(osoba.items())
