from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
raking = []

for j in range(0, 4):
    jogadores[j + 1] = randint(1, 6)

print("Valores sorteados: ")
for k, v in jogadores.items():
    print(f'O jogador {k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print("   == RANKING DOS JOGADORES ==")
for i, v in enumerate(ranking):
    print(f'    {i + 1}º lugar: Jogador {v[0]} com {v[1]}')
    sleep(1)






