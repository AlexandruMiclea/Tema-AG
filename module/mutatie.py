import module.date as date
import random

def mutatie():
    cromozomi_schimbati = set()
    for i, cromozom in enumerate(date.lista_cromozomi):
        for j, gena in enumerate(cromozom):
            valoare_uniforma = random.random()
            if valoare_uniforma <= date.probabilitate_mutatie:
                cromozom_modificat = date.lista_cromozomi[i][:j]
                cromozom_modificat += '1' if gena == '0' else '0'
                cromozom_modificat += date.lista_cromozomi[i][(j + 1):]
                date.lista_cromozomi[i] = cromozom_modificat
                cromozomi_schimbati.add(i + 1)
    return sorted(list(cromozomi_schimbati))
