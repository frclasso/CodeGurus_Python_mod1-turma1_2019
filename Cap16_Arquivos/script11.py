

#listar o conteudo do deretorio

import os

#print(os.getcwd())

diretorio = os.listdir()
for file in diretorio:
    print(file)


print('Feito')
