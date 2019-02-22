#!/usr/bin/python

import random
OUTPUT="synth_data.txt"
TABLECOUNT= 10000
ROWCOUNT = 2

PLAYERS = ["PP Shaw", "KL Rahul", "CA Pujara"]
DATA_FIELDS = ["Player", "R", "B", "M", "SR"]

PATTERN = '''1 {}: {}, {} : {}, {} : {} .
2 {} : {}, {} : {}, {} : {} .
3 What is the {} of {}?\t{}\t{}
'''

'''1 Player : {}, R : {}, B : {} .
2 Player : {}, R : {}, B : {} .
3 What is the R of {}?\t{}\t1
4 What is the B of {}?\t{}\t2
5 What is the B of {}?\t{}\t2
'''

def synth_data_generate():
    f = DATA_FIELDS
    with open(OUTPUT, 'w') as file:
        for i in range(TABLECOUNT):
            v = []
            players = PLAYERS[:]
            v0 = []
            randPlayer1 = random.choice(players)
            v0.append(randPlayer1)
            players.remove(randPlayer1)
            randPlayer2 = random.choice(players)
            v0.append(randPlayer2)
            v.append(v0)
            v1 = []
            for j in range(ROWCOUNT):
                v1.append(random.randrange(10, 100))
            v.append(v1)

            v2 = []
            for j in range(ROWCOUNT):
                v2.append(random.randrange(10, 100))
            v.append(v2)

            s = random.randrange(0, 2)
            q = random.randrange(1, 3)

            pattern = PATTERN.format(f[0], v[0][0], f[1], v[1][0], f[2], v[2][0],
                                     f[0], v[0][1], f[1], v[1][1], f[2], v[2][1],
                                     f[q], v[0][s], v[q][s], s+1)

            file.write(pattern)

if __name__ == "__main__":
    synth_data_generate()
