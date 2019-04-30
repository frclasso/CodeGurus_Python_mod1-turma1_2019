#!/usr/bin/env python3


# Aplicação de menu de retaurante

# cardapio de frutos do mar
def frutos_do_mar():
    print('Nosso cardápio de Frutos do Mar')
    escolha = input("""Selecione um dos nossos pratos:
                    1 - Lagosta
                    2 - Salmão
                    3 - Lula recheada
                    4 - Ostra gratinada
                    0 - para voltar ao menu principal""")
    print()
    if escolha == '1':
        print('Voce selecionou: Lagosta grelhada ao molho de laranja com risoto ao pesto')
        confirma_prato()
        pedidos.append('Lagosta')
    elif escolha == '2':
        print('Voce selecionou: Salmão defumando com erva doce e maionese de mostarda em grãos')
        confirma_prato()
        pedidos.append('Salmão')
    elif escolha == '3':
        print('Voce selecionou: Lula recheada com cogumelos e camarões ao molho teriayaki')
        confirma_prato()
        pedidos.append('Lula')
    elif escolha == '4':
        print('Voce selecionou: Ostra gratinada')
        confirma_prato()
        pedidos.append('Ostra')
    elif escolha == '0':
        menuprincipal()

    else:
        print('Oops opção errada, escolha uma opção de 1 a 4, ou 0 para sair')
    print()


# cardapio de massas
def massas():
    global pedidos
    print('Nosso cardápio de Massas')
    escolha = input("""Selecione um dos nossos pratos:
                    1 - Lasanha
                    2 - Penne
                    3 - Ravioli
                    4 - Spaghetti
                    0 - para voltar ao menu principal""")
    print()
    if escolha == '1':
        print('Voce selecionou: Lasanha de manjericão')
        confirma_prato()
        pedidos.append('Lasanha')
    elif escolha == '2':
        print('Voce selecionou: Penne com frango ao molho branco')
        confirma_prato()
        pedidos.append('Penne')
    elif escolha == '3':
        print('Voce selecionou: Ravioli com molho de cogumelos e espinafre')
        confirma_prato()
        pedidos.append('Ravioli')
    elif escolha == '4':
        print('Voce selecionou: Spaghetti ao molho funghi')
        confirma_prato()
        pedidos.append('Spaghtti')
    elif escolha == '0':
        menuprincipal()
    else:
        print('Oops opção errada, escolha uma opção de 1 a 4, ou 0 para sair')
    print()


# cardapio de carnes
def carnes():
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



def imprime_pedido():
    for pedido in pedidos:
        return pedido


print(imprime_pedido())

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
        elif opcao == '1':
            massas()
            break
        elif opcao == '2':
            carnes()
            break
        elif opcao == '3':
            frutos_do_mar()
            break
        elif opcao == '4':
            print(pedidos)
            break
        else:
            print('Oops opção errada, escolha uma opção de 1 a 4, ou 0 para sair')
            break


menuprincipal()   # chamando funcao menu


