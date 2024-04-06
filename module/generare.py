import random

def genereaza_cromozomi(lungime_cromozom, dimensiune_populatie):
    # generez aleator valori in intervalul [0,2**l_c - 1]

    return [bin(random.randint(0, 2**lungime_cromozom))[2:].zfill(lungime_cromozom) for x in range(dimensiune_populatie)]