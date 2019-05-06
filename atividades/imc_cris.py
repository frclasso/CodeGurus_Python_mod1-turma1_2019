#imc = peso / altura * altura
#input
#criar um menu com osparametros


print('Vamos calcular seu Indice de massa corporal!')
input('Digite Enter para comecar!')

altura = 0
peso = 0
while peso<=0:
    peso = float(input('Por favor digite seu peso: '))
    if peso<=0:
        print('Digite um valor maior que 0!')



while altura<=0 or altura>=3:
    altura = float(input('Por favor digite sua altura: '))
    if altura <=0:
        print('Digite um valor maior que 0!')
    elif altura >=3:
        print('Você é uma girafa, seu IMC deve ser calculado diferente!')

IMC = peso/altura**2

if IMC <18.5:
    print('Você esta abaixo do peso!')
    print()
elif IMC >18.5 and IMC <24.9:
    print('Parabéns seu peso esta normal!')
    print()
elif IMC <=25:
    print('Cuidado você esta em sobrepeso')
    print()
elif IMC >25 and IMC <29.9:
    print('Cuidado você esta em pré-obesidade!')
    print()
elif IMC >30 and IMC <34.9:
    print('Cuidado você esta em grau de obesidade I!')
    print()
elif IMC >35 and IMC <39.9:
    print('Cuidado você esta em grau de obesidade II!')
    print()
elif IMC >40:
    print('Cuidado você esta em grau de obesidade III!')
    print()
print('O seu IMC e', round(IMC,2))