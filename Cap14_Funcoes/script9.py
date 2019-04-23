
# *args ==> tupla
# **kwargs ==> dicionario

# ordem variveis simples, *args, argumentos padrao(=), **kwargs


def info(nome, sobrenome, *args, cidade='Florianopolis',**kwargs):
    return nome, sobrenome, args, kwargs, cidade


print(info('Fabio','Classo', 40, '99998888', 'brasileiro', funcao='programador', etinia='pardo'))