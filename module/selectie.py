import random
import module.date as date
from module.codificare import decodificare

def probabilitati_selectie():
    # intoarce un tuplu de forma:
    # (lcp, ip)
    # ip -> intervalul de probabilitati
    # lcp -> lista de tupluri de forma cromozom, probabilitate
    fitness_total = sum([date.functie (decodificare(x)) for x in date.lista_cromozomi])

    lcp = [(date.functie (decodificare(x)) / fitness_total) for x in date.lista_cromozomi]
    #for x in lcp:
    #    print(x)

    ip = tuple([(sum([date.functie (decodificare(x)) for x in date.lista_cromozomi][:i + 1]) / fitness_total) for i in range(date.dimensiune_populatie)])
    #print(ip)
    return lcp, ip#return fitness_total

def selectie():
    # cautarea se face cu cautare binara boss
    ans = []
    for numar_alegere in range(date.dimensiune_populatie):
        valoare_uniforma = random.random()
        #print(valoare_uniforma)
        l = [x if x <= valoare_uniforma else 0 for x in date.interval_probabilitati]
        fit_value = max([x if x <= valoare_uniforma else 0 for x in date.interval_probabilitati])
        #print(fit_value)

        try:
            index_cromozom = date.interval_probabilitati.index(fit_value)
            assert(valoare_uniforma >= fit_value)
        except:
            # exceptia se intampla atunci cand valoarea aleatoare este mai mica decat primul element
            # din lista intervalurilor de probabilotati, caz in care asignez primul cromozom
            index_cromozom = 0
            # print()
            # print("eroare")
            # print(valoare_uniforma)
            # print(fit_value)
            # print(date.interval_probabilitati[0])
            # print()
        ans.append((index_cromozom + 1, valoare_uniforma))
        
    return ans