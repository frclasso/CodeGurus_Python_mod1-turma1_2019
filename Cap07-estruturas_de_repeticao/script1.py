# loops / laços

id = ('20190001', '20190002', '20190003', '20190004', '20190005')

alunos = ['Fabio','Lazaro', 'Cristiane', 'Luliana', 'Joao']

# for nome in alunos:
#     print(nome)
#
# print()

# contador = 0
# while contador < len(alunos):
#     print(contador, alunos[contador])
#     contador += 1


for nome in alunos:
    if nome == 'Luliana':
        break  # troque para continue, pass
    print(nome)


