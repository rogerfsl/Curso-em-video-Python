print('=' * 25)
print('  Analisador de numeros  ')
print('=' * 25)

n = cont = s = 0

while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'No total foram digitados {cont} numeros e a soma deles é {s}!')
