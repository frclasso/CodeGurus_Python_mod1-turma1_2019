# #revisao
#
# # variaveis
# # estruturas de dados compostas (listas, tuplas, dicionarios e sets)
# # estruturas de decisao, if, elif e else
# # estruturas de repeticao
#
# fruta = 'maça' # variaveis
#
# # estruturas de decisao
# if fruta == 'banana':
#     print('Bananas são fonte de potássio')
# elif fruta == 'maça':
#     print('Maças são saborosas')
# else:
#     print('Nope')
#
# print()
#
# frutas = ['banana','abacaxi', 'limao', 'pera', 'maça'] # estruturas de dados compostas
#
# # estruturas de repeticao
# for fruta in frutas:
#     print(fruta)
#
# print()
#
# i = 0
# while i < len(frutas):
#     print(frutas[i])
#     i += 1
#
menu_principal = [
    ['Frutos do Mar'],
    ['Massas'],
    ['Carnes'],
    ['Sobremesas'],
]


frutos_do_mar = [
    {'lagosta':'1.1 - Lagosta grelhada ao molho de laranja com risoto pesto'},
    {'salmao':'1.2 - Salmão defumado com erva doce e maionese de mostarda em grão'},
    {'lula':'1.3 - Lula recheada com cogumelos e camarões ao molho teriyaki'},
]


for x in frutos_do_mar:
    for key,value in x.items():
        print(value)