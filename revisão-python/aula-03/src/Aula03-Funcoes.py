# funcoes em python
import datetime
import random


def soma (numero1, numero2):
    return numero1 + numero2

print(soma(2,7))

###########################################

def mensagem():
    print("Olá, tudo bem?")

mensagem()

############################################

print(datetime.datetime.now()) #Data atual
agora = datetime.datetime.now()
print(agora.hour) # Hora atual
print(agora.minute) # Minuto
print(agora.second) # Segundo

print(agora.day) # Dia
print(agora.month) # Mês
print(agora.year) # Ano

############################################

print(random.random()) # Número aleatório entre 0 e 1
print(random.randint(1,10)) # Número aleatório entre 1 e 10
