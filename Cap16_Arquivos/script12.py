#/usr/bin/env python3


empregados = [
    ['Fabio','Classo','fabioclasso@email.com'],
    ['Peter', 'Parker', 'pparker@email.com'],
    ['Mary','Jane', 'mjewatson@email.com'],
]

# # ler dados
# print(empregados[0])
# print(empregados[1])
# print(empregados[2][0])
#
# # modificar
# empregados[2][1] = 'Watson'
# print(empregados[2])
#
# # deletar
# #del empregados[1]
# # empregados.pop(0)
# empregados[1].remove('Peter')
# print(empregados)


# salvar em arquivo
arquivo = open('pessoas.txt', 'w')
for linha in empregados:
        arquivo.write(str(linha)+ '\n')

