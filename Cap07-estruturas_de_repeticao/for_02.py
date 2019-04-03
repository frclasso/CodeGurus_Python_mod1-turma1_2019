# for else

numbers = [11, 33,55,39,15,75,21,37,21,23,40,13]

for n in numbers:
    if n % 2 == 0:
        print('Esse numero número eh par: {}'.format(n))
        break
    else:
        print('Esse numero  NAO  eh par: {}'.format(n))
