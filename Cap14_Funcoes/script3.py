#  global vs local


x = 100  # variavel global , acessível a todas funções

print(f'Valor de x fora da funcao:{x}')


def muda_valor():
    global x  # alterar o valor da variavel global
    x = 200  # variavel local
    print(f'Valor de x dentro da função:{x}')


muda_valor()

print('Valor de x fora da funcao:{}'.format(x))

