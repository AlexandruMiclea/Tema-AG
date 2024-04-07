import random

import module.date as date
from module.codificare import decodificare
from module.incrucisare import incrucisare
from module.mutatie import mutatie
from module.selectie import probabilitati_selectie, selecteaza_elite, selectie


def afisare_cariotip(mesaj):
    date.outfile.write(mesaj + "\n")
    for i, x in enumerate(date.lista_cromozomi):
        valoare_decodificata = decodificare(x)
        date.outfile.write(f"{i + 1}: {x}".rjust(26) + " x = ")
        numar_caractere = len(
            str(
                max(
                    abs(date.domeniu_de_definitie[0]), abs(date.domeniu_de_definitie[1])
                )
            )
        )
        numar_caractere += 2 + date.precizie_discretizare
        date.outfile.write(
            f"{str(valoare_decodificata)[:(numar_caractere - (1 if valoare_decodificata > 0 else 0))]}".rjust(
                numar_caractere
            )
            + " f = "
        )
        date.outfile.write(str(date.functie(valoare_decodificata)) + "\n")
    date.outfile.write("\n")


def afisare_cariotip_elite():
    date.outfile.write("Elitele din aceasta generatie: \n")
    for i, x in enumerate(date.elite):
        # print(x)
        valoare_decodificata = decodificare(x[0])
        date.outfile.write(f"{i + 1}: {x[0]}".rjust(26) + " x = ")
        numar_caractere = len(
            str(
                max(
                    abs(date.domeniu_de_definitie[0]), abs(date.domeniu_de_definitie[1])
                )
            )
        )
        numar_caractere += 2 + date.precizie_discretizare
        date.outfile.write(
            f"{str(valoare_decodificata)[:(numar_caractere - (1 if valoare_decodificata > 0 else 0))]}".rjust(
                numar_caractere
            )
            + " f = "
        )
        date.outfile.write(str(date.functie(valoare_decodificata)) + "\n")
    date.outfile.write("\n")


afiseaza = True
afisare_cariotip("Populatia initiala:")

date.maxim_generational.append(
    (
        max([date.functie(decodificare(x)) for x in date.lista_cromozomi]),
        sum([date.functie(decodificare(x)) for x in date.lista_cromozomi])
        / date.dimensiune_populatie,
    )
)

while date.numar_etape:
    date.numar_etape -= 1

    date.lista_probabilitati, date.interval_probabilitati = probabilitati_selectie()

    date.elite = selecteaza_elite()
    if afiseaza:
        afisare_cariotip_elite()

    for x in date.elite:
        date.lista_cromozomi.remove(x[0])

    date.lista_probabilitati, date.interval_probabilitati = probabilitati_selectie()

    if afiseaza:
        date.outfile.write("Probabilitati selectie\n")
        for i in range(date.dimensiune_populatie - date.elite_per_generatie):
            date.outfile.write(
                f"cromozom {str(i + 1).rjust(3)} probabilitate {date.lista_probabilitati[i]}\n"
            )
        date.outfile.write("\n")
        date.outfile.write("Intervale probabilitati selectie\n")
        date.outfile.write("0 ")
        for elem in date.interval_probabilitati:
            date.outfile.write(str(elem) + " ")
        date.outfile.write("\n\n")

    date.lista_probabilitati, date.interval_probabilitati = probabilitati_selectie()
    rez = selectie()

    if afiseaza:
        for x in rez:
            date.outfile.write(f"u = {round(x[1], 18)}".ljust(24) + " ")
            date.outfile.write(f"selectam cromozomul {x[0]}\n")

    date.lista_cromozomi = [date.lista_cromozomi[i - 1] for i in [el[0] for el in rez]]
    if afiseaza:
        date.outfile.write("\n")
        afisare_cariotip("Populatia dupa selectie:")

    if afiseaza:
        date.outfile.write(
            f"Probabilitatea de incrucisare {date.probabilitate_incrucisare}\n"
        )
    aux = []
    for i, x in enumerate(date.lista_cromozomi):
        valoare_uniforma = random.random()
        if afiseaza:
            date.outfile.write(f"{i + 1}: {x}".rjust(26) + " u = ")
            date.outfile.write(str(valoare_uniforma))
        if valoare_uniforma < date.probabilitate_incrucisare:
            if afiseaza:
                date.outfile.write(f" < {date.probabilitate_incrucisare} participa")
            aux.append([i, x])
        if afiseaza:
            date.outfile.write("\n")
    if afiseaza:
        date.outfile.write("\n")

    aux = incrucisare(aux, afiseaza)
    for x in aux:
        date.lista_cromozomi[x[0]] = x[1]

    if afiseaza:
        afisare_cariotip("Dupa incrucisare:")

    if afiseaza:
        date.outfile.write(
            f"Probabilitatea de mutatie pentru fiecare gena {date.probabilitate_mutatie}\n"
        )

    elemente_modificate = mutatie()

    if afiseaza:
        date.outfile.write("Au fost modificati cromozomii:\n")
        for elem in elemente_modificate:
            date.outfile.write(str(elem) + "\n")
        date.outfile.write("\n")
        afisare_cariotip("Dupa mutatie:")

    for cromozom in date.elite:
        date.lista_cromozomi.append(cromozom[0])

    if afiseaza:
        afisare_cariotip("Dupa readaugare cromozomi elitisti:")

    date.maxim_generational.append(
        (
            max([date.functie(decodificare(x)) for x in date.lista_cromozomi]),
            sum([date.functie(decodificare(x)) for x in date.lista_cromozomi])
            / date.dimensiune_populatie,
        )
    )
    afiseaza = False

date.outfile.write("Evolutia maximului:\n")
date.outfile.write("Gen      Fitness maxim       Fitness mediu\n")
for i, elem in enumerate(date.maxim_generational):
    date.outfile.write(f"{i}: ".ljust(4))
    date.outfile.write(
        str(elem[0]).rjust(20).ljust(20) + str(elem[1]).rjust(20).ljust(20) + "\n"
    )

