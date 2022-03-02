#!/usr/bin/env python3

import csv
import random
 
with open("pokedex.txt") as pokedata:
    pokecomp = []
    pokelist = []
    csv_reader = csv.reader(pokedata)
    for row in csv_reader:
        pokelist.append(row)

    print("Here are your randomly assigned pokemon:")
    for i in range(6):
        pokenum = random.randint(1,721)
        pokecomp.append(pokelist[pokenum])

    for pokemon in pokecomp:
        print(f"{pokemon[1]} is a {pokemon[2]}/{pokemon[3]} pokemon with a base health stat of {pokemon[5]}" )
