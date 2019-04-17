# arquivos .txt


# sintaxe
# variavel = open('nome do arquivo', 'modo de abertura')
# 'r' = read/leitura
# 'w' = write/escrita  - cria um arquivo do zero, sobrescreve conteúdo
# 'a' = append/adicionar  no final do arquivo, usar com arquivos existentes




dados = ['Fabio', 'Classo','fabioclasso@email.com']

# for x in dados:
#     print(x, end=", ")


arq = open('teste.txt', 'w')
print(f'Nome do arquivo: {arq.name}')
print(f'Mode de abertura: {arq.mode}')
for x in dados:
    arq.write(x + ',')

arq.close()