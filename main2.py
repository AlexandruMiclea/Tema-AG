import module.date as date
import random
from module.codificare import decodificare
from module.selectie import probabilitati_selectie, selectie
from module.incrucisare import incrucisare
from module.mutatie import mutatie

date.maxim_generational.append(max([date.functie (decodificare(x)) for x in date.lista_cromozomi]))

while date.numar_etape:
    date.numar_etape -= 1
    date.lista_probabilitati, date.interval_probabilitati = probabilitati_selectie()
    rez = selectie()
    date.lista_cromozomi = [date.lista_cromozomi[i - 1] for i in [el[0] for el in rez]]
    aux = []
    for i, x in enumerate(date.lista_cromozomi):
        #print(f"{i + 1}: {x}".rjust(26), end = " u = ")
        valoare_uniforma = random.random()
        #print(valoare_uniforma, end = '')
        if (valoare_uniforma < date.probabilitate_incrucisare):
            #print(f" < {date.probabilitate_incrucisare} participa", end = '')
            # adauga cromozom alaturi de index in alta lista ca sa il prelucrezi
            aux.append([i, x])
    aux = incrucisare(aux)
    for x in aux:
        date.lista_cromozomi[x[0]] = x[1]
    elemente_modificate = mutatie()
    date.maxim_generational.append(max([date.functie(decodificare(x)) for x in date.lista_cromozomi]))

for elem in date.maxim_generational:
    print(elem)