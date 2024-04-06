import module.date as date
import random, copy

def incrucisare(valori):
    rez = []
    #print(len(valori))
    lista_cromozomi_nemodificati = [x[0] for x in valori]
    for x in range(len(valori) // 2):
        # aleg doua valori aleatoare din lista de cromozomi nealesi
        idx_cromozomi_aleatori = random.sample(lista_cromozomi_nemodificati, k=2)
        print(f"Recombinare dintre cromozomul {idx_cromozomi_aleatori[0] + 1} si cromozomul {idx_cromozomi_aleatori[1] + 1}")
        for i in idx_cromozomi_aleatori:
            lista_cromozomi_nemodificati.remove(i)
        punct_crossover = random.randint(0,date.dimensiune_populatie)
        print(f"{date.lista_cromozomi[idx_cromozomi_aleatori[0]]} {date.lista_cromozomi[idx_cromozomi_aleatori[1]]} punct {punct_crossover}")
        # schimbare valori
        valori_vechi = [x for x in valori if x[0] in idx_cromozomi_aleatori]
        valori_noi = copy.deepcopy(valori_vechi)
        valori_noi[0][1] = valori_vechi[0][1][:punct_crossover] + valori_vechi[1][1][punct_crossover:]
        valori_noi[1][1] = valori_vechi[1][1][:punct_crossover] + valori_vechi[0][1][punct_crossover:]
        print(f"Rezultat {valori_noi[0][1]} {valori_noi[1][1]}")
        for x in valori_noi:
            rez.append(x)

        # stergere valori vechi si inlocuirea cu cele noi
        for elem in valori_vechi:
            valori.remove(elem)
        print()

    if valori != []:
        print(f"Cromozomul {valori[0][0] + 1} ramane neincrucisat")
        print()
        rez.append(valori[0])
    return rez