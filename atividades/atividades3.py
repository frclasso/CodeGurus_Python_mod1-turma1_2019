# vamos criar menu

# restaurante


menu_principal = [
    ['Frutos do Mar'],
    ['Massas'],
    ['Carnes'],
    ['Sobremesas']

]

frutos_do_mar = [
    {'lagosta':'1.1 - Lagosta grelhada ao molho de laranja com risoto pesto'},
    {'salmao':'1.2 - Salmão defumado com erva doce e mainose de mostarda em grão'},
    {'lula': '1.3 - Lula recheada com cogumelos e camarões ao molho teriyaki'}
]


massas = []
carnes = []
sobremesas = []

# print(menu_principal[1])
print("Seja bem vindo resutarante delicias de Florianópolis")

print("""
    Menu:
    1) Para Frutos do Mar
    2) Para Massas
    3) Para Carnes
    4) Para sobremesas
    0) Para sair
""")

menu = input("Selecione seu pedido em nosso menu: ")
print()

while menu != '0':
    if menu == '0':
        print('Você saiu')
        break
    elif menu == '1':
        print('Voce selecionou o cardápio: {}'.format(menu_principal[0]))
        print()
        print('Em nosso cardápio de {}, temos:'.format(menu_principal[0]))
        print('-'* 53)

        for opcao in frutos_do_mar:
            for nome,valor in opcao.items():
                print(valor)

        print()
        menu = input("Selecione seu pedido em nosso menu: ")

        if menu == '1.1':
            print()
            print('Voce selecionou {}'.format(frutos_do_mar[0]['lagosta']))
        elif menu == '1.2':
            print()
            print('Voce selecionou {}'.format(frutos_do_mar[1]['salmao']))
        elif menu == '1.3':
            print()
            print('Voce selecionou {}'.format(frutos_do_mar[2]['lula']))

        break

    elif menu == '2':
        print('Voce selecionou o cardápio: {}'.format(menu_principal[1]))
        break
    elif menu == '3':
        print('Voce selecionou o cardápio: {}'.format(menu_principal[2]))
        break
    elif menu == '4':
        print('Voce selecionou o cardápio: {}'.format(menu_principal[3]))
        break
    else:
        print("Ops, acho que você nao fez a escolha certa.")
        print("Selecione um pedido de 1 a 4 ou 0 para sair")
        break





#### menu principal
# frutos do mar
   # Lagosta
   # Salmao
   # Siri
       # imprimr ingredientes  (lista de ingredientes)
# carnes
# massas
# sobremesas