
def linguagens(*args):
    if len(args) >= 1:
        for l in args:
            print(l)
    else:
        print('Error,menos de um elemento')


linguas = ['Python', 'Django', 'C#', 'Pearl', 'Haskel', 'Ruby']


linguagens(linguas)