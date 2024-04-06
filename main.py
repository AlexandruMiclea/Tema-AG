import module.date as date
import random
from module.codificare import decodificare
from module.selectie import probabilitati_selectie, selectie
from module.incrucisare import incrucisare
from module.mutatie import mutatie

def afisare_cariotip(mesaj):
    print(mesaj)
    for i, x in enumerate(date.lista_cromozomi):
        #print(decodificare(x, domeniu_de_definitie[0], precizie_discretizare, pas_discretizare))
        valoare_decodificata = decodificare(x)
        #print(f"{f"{i + 1}: {x}".rjust(26)} x = {valoare_decodificata} f = {functie (valoare_decodificata)}")
        print(f"{i + 1}: {x}".rjust(26), end = " x = ")
        # numarul de cifre pe care le poate avea partea intreaga
        numar_caractere = len(str(max(abs(date.domeniu_de_definitie[0]), abs(date.domeniu_de_definitie[1]))))
        numar_caractere += 2 + date.precizie_discretizare # numar un minus si un punct pe langa partea fractionara
        print(f"{str(valoare_decodificata)[:(numar_caractere - (1 if valoare_decodificata > 0 else 0))]}".rjust(numar_caractere), end = " f = ")
        print(date.functie (valoare_decodificata))
    print()

afisare_cariotip("Populatia initiala:")

date.maxim_generational.append(max([date.functie (decodificare(x)) for x in date.lista_cromozomi]))

#print(probabilitati_selectie())
date.lista_probabilitati, date.interval_probabilitati = probabilitati_selectie()

print("Probabilitati selectie")
for i in range(date.dimensiune_populatie):
    print(f"cromozom {str(i + 1).rjust(3)} probabilitate {date.lista_probabilitati[i]}")
print()

print("Intervale probabilitati selectie")
print(*date.interval_probabilitati)
print()

rez = selectie()

for x in rez:
    print(f"u = {round(x[1], 18)}".ljust(24), end = ' ')
    print(f"selectam cromozomul {x[0]}")

date.lista_cromozomi = [date.lista_cromozomi[i - 1] for i in [el[0] for el in rez]]
print()

afisare_cariotip("Populatia Dupa selectie:")

# incrucisare

print(f"Probabilitatea de incrucisare {date.probabilitate_incrucisare}")
aux = []
for i, x in enumerate(date.lista_cromozomi):
    print(f"{i + 1}: {x}".rjust(26), end = " u = ")
    valoare_uniforma = random.random()
    print(valoare_uniforma, end = '')
    if (valoare_uniforma < date.probabilitate_incrucisare):
        print(f" < {date.probabilitate_incrucisare} participa", end = '')
        # adauga cromozom alaturi de index in alta lista ca sa il prelucrezi
        aux.append([i, x])
    print()
print()

aux = incrucisare(aux)
for x in aux:
    date.lista_cromozomi[x[0]] = x[1]

afisare_cariotip("Dupa incrucisare:")

# mutatie

print(f"Probabilitatea de mutatie pentru fiecare gena {date.probabilitate_mutatie}")

elemente_modificate = mutatie()
print("Au fost modificati cromozomii:")
for elem in elemente_modificate:
    print(elem)
print()

afisare_cariotip("Dupa mutatie:")

date.maxim_generational.append(max([date.functie(decodificare(x)) for x in date.lista_cromozomi]))

for elem in date.maxim_generational:
    print(elem)