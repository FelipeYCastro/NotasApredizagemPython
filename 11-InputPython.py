# Entrada de dados pelo usuario em Python
# Input () do tipo str

import os#importa o cls para limpar a tela

nome = input ('Digite seu nome?') #mensagem ao usuario

idade = int (input('Digite sua idade?'))
os.system("cls")#comando para limpar a tela

print ('Se nome é ',nome)
print ('Sua idade é ',idade)