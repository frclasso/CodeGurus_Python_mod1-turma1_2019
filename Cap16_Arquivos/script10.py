

# read/ler


with open('pessoas.txt', 'r') as arq:
    with open('pessoas-copy.txt', 'w') as file:
        for line in arq:
            print(line, end='')
            file.write(line)



print('Feito')

