''' Loop FOR()
Um laço for é utilizado para iteração através de uma sequência (isto é , quer uma 
lista, uma tupla, um dicionario ou uma string)

for varName in listName:
    <bloco execução>

lista= [1,2,3,4,5]

for x in lista:
    print (x)
'''

'''
A função RANGE()
Para percorrer um conjunto de códigos um número especificado de vezes, podemos usar a função range(),
A função range() retorna uma sequência de números  iniciando em 0(zero) por padrão e incremento em 1(por padrão),
e termina em um número determinado

for x in range(10):
    print(x)
'''

lista= [1,2,3,4,5,6]
for item in lista:
    print(item)

curso = 'Curso de Python'#se colocar a chave no curso de python fica tudo na mesma linha
for x in curso:
    print(x)

for x in range(11):
    print (x)

for x in range(0, 11, 2): #pula de 2 em 2
    print (x)