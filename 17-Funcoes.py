''' Funções em Python
Uma função é um bloco de código que só é executado quando é chamado.
Voçê pode passar dados, conhecidos como parâmentros, para uma função.
Uma função pode retornar dados como resultado.

Criando uma função
Em Python, uma função é definida usando a palavra-chave DEF: 

def fn():
    <bloco execução>

def minha_funcao():
    print ('Olá eu sou uma função')

def fnComHumArgumento(arg1):
    <bloco execução>

def fnComDoisArgumento(arg1,arg2):
    <bloco execução>

'''

#CRIANDO a FUNÇÃO
def minha_funcao():
    print ('Olá eu sou uma função')

#CHAMAR A FUNÇÃO
minha_funcao()

#CRIANDO A FUNÇÃO
def minha_funcao2(mensagem):
    return(mensagem)

print (minha_funcao2('Olá eu sou a função 2'))

#CRIANDO A FUNÇÃO
def minha_funcao3(mensagem, nome):
    return(mensagem, nome)

print (minha_funcao3('Olá eu sou a função 3',' Fazer o que'))