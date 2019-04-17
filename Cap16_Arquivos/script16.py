import csv

with open('empregados.csv', 'r') as file:
    leitor = csv.reader(file, delimiter=',')
    for linha in leitor:
        print(linha)