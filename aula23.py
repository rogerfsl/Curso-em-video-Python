try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except(ValueError, TypeError):
    print('Tivemos um problema com os tipos de daos que você digitou!')
except ZeroDivisionError:
    print('Não é possivel dividir o número por 0')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado é {erro.__cause__ }')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')
