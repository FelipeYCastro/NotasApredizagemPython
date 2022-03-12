'''Lista em Python
List [ ]
Uma lista é uma coleção que é ordenada e mutável, as listas são escritas com
colchetes[ ].
'''
lista = ["maça", "banana", "uva"]
print (lista[2])

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
lista4.append ('Abacaxi')
print (lista4)