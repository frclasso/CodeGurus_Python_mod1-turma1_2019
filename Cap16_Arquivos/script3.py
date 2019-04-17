

# read/ler

arq = open('teste.txt', 'r')
str = arq.read()  # read() lê todo conteúdo do arquivo
print(str)
arq.close()