jog = {}
gols = []
jogadores = []

while True:
    jog.clear()
    gols.clear()
    jog['nome'] = input("Nome do jogador: ").strip().upper()
    partidas = int(input(f"Quantos jogos {jog['nome']} participou? "))
    for p in range(0, partidas):
        gols.append(int(input(f'Quantos gols no jogo {p + 1}? ')))
    jog['gols'] = gols
    jog['total'] = sum(gols)
    jogadores.append(jog.copy())

    resp = input("Quer continuar? [S | N] ").strip().upper()[0]
    while resp not in 'SsNn':
        resp = input("Quer continuar? [S | N] ").strip().upper()[0]
    if resp == 'N':
        break

print('-=-' * 25)
print('cod ', end='')
for i in jog.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 25)
for k, v in enumerate(jogadores):
    print(f'{k:>3}', end=' ')
    for j in v.values():
        print(f'{str(j):<14}', end=' ')
    print()
print('-' * 25)

while True:
    busca = int(input("Quer saber os dados de qual jogador? (999 ENCERRA) "))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f"Erro! Não existe jogador com código {busca}")
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores [busca] ["nome"]}:')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
print("--   PROGRAMA FINALIZADO    --")
"""while True:
    jog.clear()
    gols.clear()
    jog['nome'] = input('Nome do jogador: ').strip().upper()
    partidas = int(input(f"Quantas partidas {jog['nome']} jogou? "))
    for p in range(0, partidas):
        gols.append(int(input(f"Quantos gols na partida {p + 1}? ")))
    jog['gols'] = gols[:]
    jog['total'] = sum(gols[:])
    jogadores.append(jog.copy())

    resp = input("Quer continuar? [S | N] ").strip().upper()[0]
    while resp not in 'SsNn':
        resp = input("Quer continuar? [S | N] ").strip().upper()[0]
    if resp == 'N':
        break
print('-=-' * 30)
print('cod ', end='')
for i in jog.keys():
    print(f'{i:<15}', end='')
print()
print('-=-' * 30)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    opc = int(input("Deseja ver os dados de que jogador? (999 encerra!) "))
    if opc == 999:
        print("Programa finalizado!")
        break
    if opc >= len(jogadores):
        print(f'ERRO! não existe com o código {opc}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[opc]["nome"]} --')
        for i, g in enumerate(jogadores[opc]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-=-' * 30)

print("Programa finalizado!")
"""