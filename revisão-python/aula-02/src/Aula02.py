#If, elif e else


nota = float (input("Digite a nota: "))
if nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Recuperação!")
else:
    print("Reprovado!")

letra = input("Digite uma letra: ").lower()
if letra in "aeiou":
    print("É uma vogal")
else:
    print("É uma consoante")

#Verificar se o ano é bissexto

ano = int(input("Digite um ano: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Ano bissexto")
else:
    print("Ano normal")

# Estrutura While

x = 1
while x <=10:
    print(x)
    x += 1

# Loop infinito

y = 1
while True:
    print(y)

z = 2
while z == 2:
    print(z)


# Tabuada adição (contador)

n = int (input("Digite um número: "))
x = 1 #contador

while x <=10:
    print(n+x)
    x += 1


# Tabuada adição (contador)

x = 1
soma = 0 #acumulador
while x <= 10:
    n = int(input("Digite um número: "))
    soma = soma + n
    x = x + 1
print(soma)


#interromper repetição

x = 1
while x <= 10:
    if x == 7:
        break
    print(x)
    x += 1



import time

print("SORTEIO")
x = 0
while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break
    x = x + num
print("Somando...")
y = 5
while y <= 5:
    time.sleep(1)
    print(y)
    y = y - 1
    if y == 0:
        break
print("A soma é:", x)

for i in range(5):
    print(i)


for x in range (1,11):
    print(x)


for c in "Python":
    print(c)


lista = [1,2,3,4,5,6,7,8,9]
for item in lista:
    print(item)

lista2 = ['Processador', 'Memória', 'Teclado', 'Mouse']
for item in lista2:
    print(item)



import random

numero = random.randint(1,10)
print(numero)
