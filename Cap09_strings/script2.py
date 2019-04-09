# capitulo 16

# arquivos

alunos = ['Fabio','Lazaro', 'Cristiane', 'Luliana', 'Joao']

with open('arquivo.txt', 'a') as file:
    for aluno in alunos:
        file.writelines(aluno + '\n')

print('Feito')