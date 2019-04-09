
# login

secret = 'swordfish'
senha = ''

while senha != secret:
    senha = input('Digite senha: ')

    if senha == secret:
        print('Voce esta logado')
        print()
    else:
        print('Senha incorreta')
        print()
