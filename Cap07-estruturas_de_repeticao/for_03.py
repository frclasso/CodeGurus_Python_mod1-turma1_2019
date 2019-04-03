# loop aninhado


lot_2D = [
    ['Toyota', 'Audi', 'BMW'],
    ['Lexus', 'Jeep'],
    ['Honda', 'Kia', 'Mazda']
]

#print(lot_2D[0][0])  # lista 0 , elemento 0 da lista 0

# for linha in lot_2D:
#     for carro in linha:
#         print(carro)

lot_3D =[
    [
        ['Tesla', 'Fiat', 'BMW'],
        ['Honda', 'Jeep'],
        ['Saab','Kia', 'Ford']
    ],
    [
        ['Subaru', 'Nissan'],
        ['Volkswagen'],
        ['Mercedez']
    ],
    [
        ['Chevrolet', 'GMC'],
        ['Ferrari', 'Lamborghini']
    ]
]
#print(lot_3D[0])
# print(lot_3D[0][0])
#print(lot_3D[0][0][1])
for grupo in lot_3D:
    for line in grupo:
        for carro in line:
            print(carro)