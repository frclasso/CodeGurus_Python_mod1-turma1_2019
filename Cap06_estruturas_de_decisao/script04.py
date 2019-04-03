# ifs aninhados


num = int(input('Digite um numero: '))

if num % 2 == 0:
    if num % 3 == 0:
        print('Numero: {} divisivel por 2 e 3'.format(num))
    else:
        print('Numero: {} e divisivel por 2 e nao por 3'.format(num))
else:
    if num % 3 == 0:
        print('Numero: {} divisivel por 3 e nao por 2'.format(num))
    else:
        print('Numero: {} nao é divisivel nem por 2 nem por 3'.format(num))

print('Done...')