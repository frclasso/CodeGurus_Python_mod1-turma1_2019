

amount = int(input('Enter the amount: '))

if amount <= 1000:
    discount = amount * 0.05   # desconto de 5%
    print('Discount: {}'.format(discount))
elif amount <= 5000:
    discount = amount * 0.10 # desconto de 10%
    print('Discount: {}'.format(discount))
else:
    discount = amount * 0.15 # desconto de 15%
    print('Discount: {}'.format(discount))

print('Net payable: {}'.format(amount - discount))  # valor - desconto