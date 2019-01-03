# flip coins and track the patterns
import random

coin = ['H','T']
bothheads = 0
bothtails = 0
headsandtails = 0
TandH = 0
HandT = 0

def flip(coin):
    if random.randint(0, 21)%2 == 0:
        return coin[0]
    else:
        return coin[1]


for n in range(20000):
    coin1 = flip(coin)
    coin2 = flip(coin)

    print(coin1, coin2)
    if coin1 == "T" and coin2 == "T":
        bothtails += 1
    elif coin1 == "H" and coin2 == "H" :
        bothheads += 1
    else:
        if coin1 == "H" and coin2 == "T":
            HandT += 1
        if coin1 == "T" and coin2 == "H":
            TandH +=1
        headsandtails += 1

print('Occurrences of both heads: ', bothheads)
print('Occurrences of both tails: ', bothtails)
print('Occurrences of mixed results: ', headsandtails)
print("Specifically  ", HandT, " first coin heads and second tails", end= " ")
print(" and ", TandH, " first coin tails and the second heads "  )