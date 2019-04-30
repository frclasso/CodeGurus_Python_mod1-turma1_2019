

pedidos = []

valores = {'Lasanha':50,
     'Penne':45,
     'Ravioli':40,
     'Spagheti':35
     }


# cardapio de carnes
def carnes():
    global pedidos
    print('Nosso cardápio de Carnes')
    escolha = input("""Selecione um dos nossos pratos:
                    1 - Carne de Panela
                    2 - Contra filé
                    3 - Filé ao molho madeira
                    4 - Carne louca
                    0 - para voltar ao menu principal""")
    print()
    if escolha == '1':
        print('Voce selecionou: Carne de Panela com batatas, acompanha arroz e salada ')
        confirma_prato()
        pedidos.append('Carne de Panela')
    elif escolha == '2':
        print('Voce selecionou: Contra filé, com cenoura, cebola, pimentão e queijo muçarela')
        confirma_prato()
        pedidos.append('Contra filé')
    elif escolha == '3':
        print('Voce selecionou: Filé ao molho madeira, acompanha arroz e fritas')
        confirma_prato()
        pedidos.append('Filé ao molho madeira')
    elif escolha == '4':
        print('Voce selecionou: Carne louca cremosa, acompanha torradas e salada verde')
        confirma_prato()
        pedidos.append('Carne louca')
    elif escolha == '0':
        menuprincipal()
    else:
        print('Oops opção errada, escolha uma opção de 1 a 4, ou 0 para sair')
    print()


def confirma_prato():
    print()
    escolha = input("Confirma o prato selecionado? 's' para sim , 'n' para voltar ao menu principal")
    if escolha == 's':
        print("Prato confirmado, em poucos minutos seu prato estará pronto")
        print()
        menuprincipal()
    else:
        menuprincipal()


pedidos = []

valores = {
    'Lasanha':50,
    'Penne':45,
    'Ravioli':40,
    'Spagheti':35
}



def menuprincipal():
    opcao = input("""Seja bem vindo ao nosso restaurante, escolhar uma opção:
                    1 - Para Massas
                    2 - Para carnes
                    3 - Para Frutos do Mar
                    4 - Fechar pedido
                    0 - Para sair: """)

    while True:
        if opcao == '0':
            print('Sair')
            break
        elif opcao == '2':
            carnes()
            break
        elif opcao == '4':
            print(pedidos)
            break
        else:
            print('Oops opção errada, escolha uma opção de 1 a 4, ou 0 para sair')
            break


menuprincipal()   # chamando funcao menu

print(pedidos)
