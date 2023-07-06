from time import sleep

print('=' * 11)
print('  TABUADA ')
print('=' * 11)

t = 0

while True:

    n = int(input('Quer saber a tabuada de qual valor? '))
    print('-' * 35)

    cont = 0
    if n < 0:
        break

    while cont < 10:
        cont += 1
        t = n * cont
        print(f'{n} x {cont:2} = {t}')
    sleep(0.5)
    print('-' * 35)
print('Programa de tabuada encerrado!')

