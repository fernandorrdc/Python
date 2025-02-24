#dicionário

#formas de criação
dicionario = {}
dicionario = dict()

dicionario = {'nome' : 'Quemich' , 'idade' : 29 , 'altura' : 1.79}
print(dicionario)

#acessando posição
print(dicionario['nome'])

# adcionando elementos 
dicionario['programador'] = 'Pyton'
print(dicionario)

#sobrescrevendo 
dicionario['idade'] = 25
print(dicionario)

#percorrer dicionário
"""for var in dicionario:
    print(var)
"""
for key in dicionario:
    print(key ,dicionario[key])

#testado a existencia de uma key n estrutura

print('sobrenome' in dicionario)
print('nome' in dicionario)

