# -*-coding:utf-8-*-


# funcoes
# definindo uma funcao

# def nome():
#     pass

# chamanda de funcao (executar)
# nome()
def soma(x,y):
    return x + y


def multi(x,y):
    return x * y


def printme():
    """Imprime uma string  que foi passada como argumento para a funcao """
    print(soma(4,5))
    print(multi(4,5))


printme()


def printme(funcao):
    """Imprime uma string  que foi passada como argumento para a funcao """
    print(funcao)


printme(soma(10,20))