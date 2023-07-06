pessoa = {}
galera = []
media = soma = 0

while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ').strip().upper()
    pessoa['sexo'] = input('Sexo [M | F]: ').upper().strip()[0]
    while pessoa['sexo'] not in 'MmFf':
        pessoa['sexo'] = input('Sexo [M | F]: ').upper().strip()[0]
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    resp = input("Quer continar? [S | N] ").strip().upper()[0]
    while resp not in 'SsNn':
        resp = input("Quer continar? [S | N] ").strip().upper()[0]

    if resp == 'N':
        break

print(f'A) Foram cadastradas {len(galera)} pessoas.')
media = soma / len(galera)
print(f'B) A média de idade das pessoas cadastradas é {media:5.2f}')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}...', end=' ')
print()
print(f'D) Lista das pessoas cadastradas que estão acima da média de idade:')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
        print()

"""while True:
    pessoas.clear()
    pessoas['nome'] = input("Nome: ").strip().upper()
    pessoas['sexo'] = input('Sexo [M | F] ').strip().upper()[0]
    while pessoas['sexo'] not in 'MmFf':
        pessoas['sexo'] = input('Sexo [M | F] ').strip().upper()[0]
    pessoas['idade'] = int(input("Idade: "))
    soma += pessoas['idade']
    galera.append(pessoas.copy())

    resp = input("Quer continuar? [S | N] ").strip().upper()[0]
    while resp not in "SsNn":
        resp = input("Quer continuar? [S | N] ").strip().upper()[0]
    if resp == 'N':
        break

print('-=-' * 30)
print(f"A) Foram cadastradas {len(pessoas)} pessoas.")
media = soma / len(pessoas)
print(f'B) A media de idade das pessoas cadastradas é {media:5.2f}')
print("C) Lista com as mulheres cadastradas: ", end='')
for i in galera:
    if i['sexo'] == 'F':
        print(f'{i["nome"]}', end=' ')
print('\nC) Lista com as pessoas com idade acima da média: ')
for i in galera:
    if i["idade"] > media:
        for k, v in i.items():
            print(f'{k} = {v}', end='; ')"""
