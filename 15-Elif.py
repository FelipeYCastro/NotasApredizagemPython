''' Pithon Id ... Else

if < condição > :
    <bloco verdadeiro>
else: 
    <bloco falso>
'''

'''
Elif
A palavra-chave elif é uma forma em python de dizer se as condições anteriores 
fossem verdadeiras teste  esta condição

if < condição > :
    <bloco verdadeiro>
elif < condição > :
    <bloco verdadeiro>
else: 
    <bloco falso>

'''
import os

idade = int (input('Digite sua idade: '))

os.system('cls')#limpa tela

if idade < 18:
    print('Menor de idade')
elif idade >= 18 and idade <= 60:
    print('Adulto')
else:
    print('Idoso')