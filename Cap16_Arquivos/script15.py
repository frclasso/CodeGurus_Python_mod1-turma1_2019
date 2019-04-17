
import csv

with open('empregados.csv', 'a') as file:
    w = csv.writer(file, delimiter=',')
    w.writerow(['Jane Smith', 'Gerente','2018'])
    w.writerow(['Peter Parker', 'Spider man','2018'])
    w.writerow(['Mary Jane', 'Dancer','2018'])
    w.writerow(['Bruce Wayne', 'Batman','2018'])
    w.writerow(['Bruce Lee', 'Lutador','2018'])
    w.writerow(['Michael Jordan', 'Jogador','2018'])
    w.writerow(['Michael Jackson', 'Cantor','2018'])
    w.writerow(['Donald Trump', 'Presidente','2018'])
    w.writerow(['Darth Vader', 'Personagem','2018'])

print('Feito')



