''' DICIONÁRIO EM PYTHON
Um dicionario é uma coleção, mutavel e indexada. No Python, os dicionários, são
 com chaves e possuem chaves e valores. 

Você também pode usar funcção values () para retornar vallores de um dicionário:
Você também pode usar funcção Keys () para retornar vallores de um dicionário:
Você também pode usar funcção items () para retornar vallores de um dicionário:

No metódo pop () remove o intem com o nome de chaves especificada

ex:
dicionario = {}
dicionario = {chave : valor}
'''
dicionario = { 'A' : 'Python', 'B': 'JavaScript', 'C': 'Android'}
print (dicionario)

#ACESSANDO ITENS
print (dicionario['B'])#Vi imprimir JavaScript

#MUDAR VALORES
dicionario ['C'] = 'PHP'#vai trocar Android por PHP na lista
print (dicionario)

#PARA IMPRIMIR APENAS OS VALORES DO DICIONARIO
print (dicionario.values()) #imprimi apenas os valores
# dict_values(['Python', 'JavaScript', 'PHP'])

#PARA IMPRIMIR APENAS AS CHAVES DO DICIONARIO
print(dicionario.keys()) #retorna
# dict_keys(['A', 'B', 'C'])

#PAR IMPRIMIR OS ITEMS DO NOSSO DICIONARIO
print (dicionario.items())# vai retornar os itens 
# dict_items([('A', 'Python'), ('B', 'JavaScript'), ('C', 'PHP')])

#REMOVER ITEM
dicionario.pop('C')#vai apagar o item 'C'
print(dicionario)