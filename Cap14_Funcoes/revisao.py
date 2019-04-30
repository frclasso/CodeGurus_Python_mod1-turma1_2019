# funcoes



# definindo a função
def nome_da_funcao():
    print("Função em execução")


# funçoes com parametros
def soma(x, y): # x, y são os paramentros
    return x + y


def mutiplica(x, y):
    return x * y

def imprimeResultado(funcao):
    print(funcao)


# imprimeResultado(soma(10,20))
# imprimeResultado(mutiplica(10,20))

def dados(nome, idade, email='fabio@email.com', *args, **kwargs):  # parametro padrao/default
    return nome, idade, email, args, kwargs


def imprimeResultado(dados):
    print(dados)


imprimeResultado(dados('Fabio', 'Classo', 1, '4899993333', 47470470470, identidade='01110101001', tituloeleitor='010101010'))

