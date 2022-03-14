#lista - list[]
#append - insert- remove - pop - del - clear


'''Lista em Python
List [ ]
Uma lista é uma coleção que é ordenada e mutável, as listas são escritas com
colchetes[ ] ela pode conter todos os tipos de dados.
'''
lista = ["maça", "banana", "uva"]
print (lista[2])

lista99 = list (range(11))#o comando list +range vai gerar números naquele range
# de números vai gerar de 0 de zero a 10
print (lista99)

'''
Você pode especificar um intervalo de índices especificando por onde começa e 
por onde termina o intervalo. Ao especificar um intervalo, o valor retorna será
uma nova lista com os itens especificados.
'''

lista2 = ["maça", "banana", "uva", "Pera", "Melão", "Abacaxi", "laranja"]
print (lista2[2:5])

''' ALTERAR VALOR DO ITEM
Para alterar o valor do item especificífivo, consulte o número do índice:
'''
lista3 = ["maça", "banana", "uva"]
lista3[2] = "ORANGE"
print (lista3[2])

''' ADICIONAR O ITEM AO FINAL DA LISTA
Metodo append()
'''
lista4 = ["maça", "banana", "uva"]
lista4.append ('Abacaxi')#adiciona no fim da lista
print (lista4)

''' ADICIONAR O ITEM AO ÍNDICE ESPECIFICADO USE O
MÉTODO insert()
'''
frutas = ["maça", "banana", "uva"]
frutas.insert (0, 'Abacaxi')#o zero significa a posição no indice
print (frutas)

''' REMOVER ITEM EXISTEM VARIAS FORMAS
O remove()método remove o item especificado
'''
frutas2 = ["maça", "banana", "uva", "Abacaxi"]
frutas2.remove ("banana")#o remove( remove o item esecifico)
print (frutas2)

#O pop()método remove o índice espeficado OU o último item se o indice não for especificado

frutas3 = ["maça", "banana", "uva", "Abacaxi"]
frutas3.pop(0)#ira remover o maça
print (frutas3)

#A palavra-chave del[0] remove o índce especificado

frutas4 = ["maça", "banana", "uva", "Abacaxi"]
del frutas4[2] #neste caso o índice 2 "uva" vai ser apagado
print (frutas4)

#LIMPA A LISTA 
frutas4.clear()
print (frutas4)#lista vai ficar vazia