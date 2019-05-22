# -*-coding:utf-8-*0-

try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    print("{}/{} = {}".format(a,b,a/b))
except ZeroDivisionError:
    print("O divisor não pode ser zero")
# except ValueError:
#     print('Valor fornecido NAO é um número inteiro')
except Exception as e:
    print('Erro desconhecido...', e)
