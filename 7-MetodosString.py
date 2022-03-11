'''Métodos de String
O Python possui um conjunto de métodos internos que voc^pode usar em strings.
O método strip ( ) remove qualquer espaço em branco do começo ou do fim.
O método lower ( ) retorna a string em letras minusculas.
O método upper ( ) retorna a string em letras maiusculas.
O método replace ( ) substitui uma stringpor outra string;
O método split ( ) divide a string em subsrtrings e encntrar instâncias do separador

Para verficar se uma determinada frase u caracter esta presente em uma string, podem
uar as palavras-chave in ou not in
'''

curso = ' Curso de Python '
print (curso)
print (curso.strip())#remove esoaço do inicio e fim

curso = ' Curso de Python '
print (curso.lower())

curso = ' Curso de Python '
print (curso.upper())

curso = ' Curso de Python '
print (curso.replace('e','3'))#substirui as letras da string

curso = ' Curso de Python '
print (curso.split()) #lista com 3 novas palavras

#in ou not in

curso = 'Curso de Python'
x = 'de' in curso #resumindo nesta variavel a palavra 'de' esta contido na frase ou seja True
y = 'de' not in curso #vai inverter o resultado negação

print (x)
print (y)