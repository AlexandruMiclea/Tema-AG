import math
from module.generare import genereaza_cromozomi

# date de intrare

dimensiune_populatie = 20 # 0...
domeniu_de_definitie = [-1, 2] # lista cu 2 capete
functie = lambda x : - (x ** 2) + (x) + 2 # lambda expresie cu ecuatia functiiei
precizie_discretizare = 6 # 0...
probabilitate_incrucisare = 0.1 # intre 0 si 1
probabilitate_mutatie = 0.01
numar_etape = 50 # 0...

# date necesare

lungime_cromozom = math.ceil(math.log2((domeniu_de_definitie[1] - domeniu_de_definitie[0])*10**precizie_discretizare))
#print(lungime_cromozom)

pas_discretizare = (domeniu_de_definitie[1] - domeniu_de_definitie[0]) / 2 ** lungime_cromozom
#print(pas_discretizare)

lista_cromozomi = genereaza_cromozomi(lungime_cromozom, dimensiune_populatie)
#print(*lista_cromozomi)

lista_probabilitati = []
interval_probabilitati = []
maxim_generational = []