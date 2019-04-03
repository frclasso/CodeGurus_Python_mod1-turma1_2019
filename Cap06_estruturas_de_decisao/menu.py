
# menu

print("""
    Menu:
    1) Para cadastrar novos usuarios
    2) Para editar dados dos usuarios
    3) Para excluir um usuario
    4) Salvar dados
    5) Para exibir todos os usuarios
    6) Para sair

""")

menu = int(input('Digite uma das opções: '))

if menu == 6:
    print('Voce saiu do programa')
elif menu == 1:
    print('Cadastro de novos usuarios')
elif menu == 2:
    print('Editar dados dos usuarios')
elif menu == 3:
    print('Excluir um usuario')
elif menu == 4:
    print('Salvar dados')
elif menu == 5:
    print('Exibir todos os usuarios')
else:
    print('ERRO: Voce precisa escolher um numero de 1 a 6')
