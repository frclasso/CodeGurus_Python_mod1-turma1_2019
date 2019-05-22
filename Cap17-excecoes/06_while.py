
# -*-coding:utf-8-*0-

while True:

    try:
        a = int(input('Digite um número: '))
        b = int(input('Digite outro número: '))
        print("{}/{} = {}".format(a,b,a/b))
    except Exception as e:
        print("Erro nao identificado", e)
    else:
        break