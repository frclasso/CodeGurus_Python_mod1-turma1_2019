

# dicionario "dict = {k : v}"

def info(**kwargs):
    for key, value in kwargs.items():
        print('O valor de {} é {}'.format(key, value))


info(nome='Fabio')
info(nome='Joao')


# d = {'Nome':'Fabio', 'idade':40}
#
# print(d.items())
# print(d.keys())
# print(d.values())
#
# for k,v in d.items():
#     print('{} é {}'.format(k,v))
