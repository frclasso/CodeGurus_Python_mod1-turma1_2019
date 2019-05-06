#!/usr/bin/env python3

# -*-coding:utf-8 -*-   

def menu_massas():
    print('Nosso cardápio de massas')
    escolha = input("""Selecione um dos pratos:
                    1 - Lasanha
                    2 - Penne
                    3 - Ravioli
                    4 - Spaghetti
                    0 - Para voltar para o menu principal""")
    print()
    if escolha == '1':
        print('Voc￿ê selecionou : Lasanha de milho e majericão')
        confirmar_prato()
    elif escolha == '2':
        print('Voc￿ê selecionou : Penne com frango ao molho branco')
        confirmar_prato()
    elif escolha == '3':
        print('Voc￿ê selecionou : Ravioli com molho de cogumelos e espinafres')
        confirmar_prato()
    elif escolha == '4':
        print('Voc￿ê selecionou : Spaghetti ao molho funghi')
        confirmar_prato()
    elif escolha == '0':
        menu_principal()
    else:
        print('Voce precisa escolher uma opção entre 1 e 4, ou 0 para menu principal.')

    print()


def menu_carnes():
    print('Nosso cardápio de Carnes')
    escolha = input("""Selecione um dos pratos:
                    1 - Carne de Panela
                    2 - Contra filé recheado
                    3 - Filé ao molho madeira
                    4 - Carne louca
                    0 - Para voltar para o menu principal""")
    print()
    if escolha == '1':
        print('Voc￿ê selecionou : Carne de panela com batatas , acompanha arroz e batatas')
        confirmar_prato()
    elif escolha == '2':
        print('Voc￿ê selecionou : Contra filé recheado, com cenoura, cebola, pimentão e queijo muçarela.')
        confirmar_prato()
    elif escolha == '3':
        print('Voc￿ê selecionou : Filé ao molho madeira, acompanha arroz e fritas')
        confirmar_prato()
    elif escolha == '4':
        print('Voc￿ê selecionou : Carne louca cremosa, acompanha torradas e salada verde')
    elif escolha == '0':
        menu_principal()
    else:
        print('Voce precisa escolher uma opção entre 1 e 4, ou 0 para menu principal.')

    print()


def menu_frutos_do_mar():
    print('Nosso cardápio de Frutos do Mar')
    escolha = input("""Selecione um dos pratos:
                    1 - Lagosta
                    2 - Salmão
                    3 - Lula recheada
                    4 - Ostra gratinada
                    0 - Para voltar para o menu principal""")
    print()
    if escolha == '1':
        print('Voc￿ê selecionou : Lagosta grelhada ao molho de laranja com risoto pesto')
        confirmar_prato()
    elif escolha == '2':
        print('Voc￿ê selecionou : Salmão defumado com erva doce e maionese de mostarda em grão')
        confirmar_prato()
    elif escolha == '3':
        print('Voc￿ê selecionou : Lula recheada com cogumelos e camarões ao molho teriyaki')
        confirmar_prato()
    elif escolha == '4':
        print('Voc￿ê selecionou : Ostra gratinada')
        confirmar_prato()
    elif escolha == '0':
        menu_principal()
    else:
        print('Voce precisa escolher uma opção entre 1 e 4, ou 0 para menu principal.')

    print()


def confirmar_prato():
    escolha = input("Confirma o prato selecionado s/n:")
    if escolha == 's':
        print("Prato confirmado, em poucos minutos estará pronto")
        menu_principal()
    else:
        menu_principal()


def sair():
    return None


def confirmar_saida():
    escolha = input("Digite 's' para sair ou 'i' para voltar ao início ")

    if escolha == 's':
        print('Obrigado por sua visita, volte sempre.')
        sair()
    else:
        menu_principal()




def menu_principal():
    opcao = input("""Seja bem vindo ao nosso restaurante, escolha um opção:
                  1 - Para Massas
                  2 - Para Carnes
                  3 - Para Frutos do Mar
                  0 - Para sair : """)

    while True:
        if opcao == '0':
            confirmar_saida()
            break
        elif opcao == '1':
            menu_massas()
            break
        elif opcao == '2':
            menu_carnes()
            break
        elif opcao == '3':
            menu_frutos_do_mar()
            break
        else:
            print('Escolha errada, escolha novamente')


menu_principal()