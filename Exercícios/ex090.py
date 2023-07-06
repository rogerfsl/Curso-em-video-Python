alunos = {}

alunos['Nome'] = input('Nome: ').strip()
alunos['Média'] = float(input(f'Media de {alunos["Nome"]}: '))

if alunos['Média'] >= 7:
    alunos['Situação'] = 'Aprovado'
elif 5 <= alunos['Média'] < 7:
    alunos['Situação'] = 'Recuperação'
else:
    alunos['Situação'] = 'Reprovado'
print("-=-" * 20)
for k, v in alunos.items():
    print(f'{k} é igual a {v}')