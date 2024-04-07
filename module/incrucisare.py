import copy
import random

import module.date as date


def incrucisare(valori, afisare):
    rez = []
    lista_cromozomi_nemodificati = [x[0] for x in valori]
    for x in range(len(valori) // 2):
        idx_cromozomi_aleatori = random.sample(lista_cromozomi_nemodificati, k=2)
        if afisare:
            date.outfile.write(
                f"Recombinare dintre cromozomul {idx_cromozomi_aleatori[0] + 1} si cromozomul {idx_cromozomi_aleatori[1] + 1}\n"
            )
        for i in idx_cromozomi_aleatori:
            lista_cromozomi_nemodificati.remove(i)
        punct_crossover = random.randint(0, date.dimensiune_populatie)
        if afisare:
            date.outfile.write(
                f"{date.lista_cromozomi[idx_cromozomi_aleatori[0]]} {date.lista_cromozomi[idx_cromozomi_aleatori[1]]} punct {punct_crossover}\n"
            )
        valori_vechi = [x for x in valori if x[0] in idx_cromozomi_aleatori]
        valori_noi = copy.deepcopy(valori_vechi)
        valori_noi[0][1] = (
            valori_vechi[0][1][:punct_crossover] + valori_vechi[1][1][punct_crossover:]
        )
        valori_noi[1][1] = (
            valori_vechi[1][1][:punct_crossover] + valori_vechi[0][1][punct_crossover:]
        )
        if afisare:
            date.outfile.write(f"Rezultat {valori_noi[0][1]} {valori_noi[1][1]}\n")
        for x in valori_noi:
            rez.append(x)

        for elem in valori_vechi:
            valori.remove(elem)
        if afisare:
            date.outfile.write("\n")

    if valori != []:
        if afisare:
            date.outfile.write(f"Cromozomul {valori[0][0] + 1} ramane neincrucisat\n")
            date.outfile.write("\n")
        rez.append(valori[0])
    return rez

