#!/usr/bin/env python3


# laço/loop de repetição while

#contador = 0

# while contador <= 5:
#     print('O número é: {}'.format(contador))
#     contador = contador + 1


contador = int(input('Insira um numero: '))

while contador < 5:
    print('O número {} é menor que 5'.format(contador))
    contador = contador + 1
else:
    print('{} nao é menor que 5'.format(contador))
print('Feito...')
