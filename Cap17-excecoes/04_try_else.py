

try:
    fh = open('arquivo.txt', 'r')
    fh.read()
except IOError:
    print('Error: Arquivo não encontrado')
else:
    print('Arquivo encontrado com sucesso.')
    fh.close()