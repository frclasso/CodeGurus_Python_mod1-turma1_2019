
# menu que vai utilizar cadastro2.py e cadastro3.py

from cadastro2 import salvaDados
from cadastro3 import leitor

# menu = cadastrar, salvarDados, leitor

menu = int(input('Escolha uma opção:'))

if menu == 1:
    salvaDados()
elif menu == 2:
    leitor()
else:
    print('Voce precisa selecionar uma das opções')



