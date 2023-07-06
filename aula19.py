estado = {}
brasil = []

for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ').strip().upper()
    estado['sigla'] = input('Sigla: ').strip().upper()
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(f'{v}', end=' ')
    print()


    """for k, v in e.items():
        print(f'O campo {k} tem valor {v}')"""

"""brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])"""

"""pessoas = {"Nome": "Gustavo", "Sexo": "M", "Idade": 22}
pessoas["Peso"] = 98.5
for k, v in pessoas.items():
    print(f"{k} = {v}")"""

# pessoas["Nome"] = "Leandro"
# del pessoas['Sexo']
# print(pessoas.items())
# print(f"O {pessoas['Nome']} tem {pessoas['Idade']} anos.")
