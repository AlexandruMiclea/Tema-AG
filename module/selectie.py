import random
import module.date as date
from module.codificare import decodificare

def probabilitati_selectie():
    fitness_total = sum([date.functie (decodificare(x)) for x in date.lista_cromozomi])

    lcp = [(date.functie (decodificare(x)) / fitness_total) for x in date.lista_cromozomi]
    ip = tuple([(sum([date.functie (decodificare(x)) for x in date.lista_cromozomi][:i + 1]) / fitness_total) for i in range(date.dimensiune_populatie)])
    return lcp, ip

def binary_search(arr, left, right, value):
    middle = (left + right) // 2
    while left <= right:
        middle = (left + right) // 2
        if (arr[middle] > value):
            right = middle - 1
        else:
            ans = arr[middle] 
            left = middle + 1
    
    return middle

def selectie():
    ans = []
    for numar_alegere in range(date.dimensiune_populatie):
        valoare_uniforma = random.random()
        fit_value = binary_search(date.interval_probabilitati, 0, len(date.interval_probabilitati), valoare_uniforma)
        ans.append((fit_value + 1, valoare_uniforma))
        
    return ans