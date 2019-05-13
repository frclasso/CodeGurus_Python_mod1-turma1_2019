

# dicionarios aninhados

funcionarios = {
    1:{'nome':'Paulo', 'idade':56, 'sexo':'masculino', 'setor':'estoque'},
    2:{'nome':'Gisele', 'idade':40, 'sexo':'feminino', 'setor':'marketing'},
    3:{'nome':'Marcela', 'idade':38, 'sexo':'feminino', 'setor':'vendas'},
}

funcionarios[4] = {}
funcionarios[4]['nome'] = 'Francisco'
funcionarios[4]['idade'] = 21
funcionarios[4]['sexo'] = 'masculino'
funcionarios[4]['setor'] = 'vendas'


funcionarios.update({5:{'nome':'Marcelo', 'idade':38, 'sexo':'masculino', 'setor':'administrativo'}})

for k, v in funcionarios.items():
    print(k, '==>', v)

print('-'*90)

# print(funcionarios[1])
# for k, v in funcionarios[1].items():
#     print(k,'=>',  v)

for f_id, f_info  in funcionarios.items():
    # print('Pessoas id:', f_id)

    for k in f_info:
        print(f_id, k, '==>',f_info[k])

