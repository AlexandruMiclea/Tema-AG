import random


def genereaza_cromozomi(lungime_cromozom, dimensiune_populatie):
    return [
        bin(random.randint(0, 2**lungime_cromozom))[2:].zfill(lungime_cromozom)
        for x in range(dimensiune_populatie)
    ]

