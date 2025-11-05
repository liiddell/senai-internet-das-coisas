#If, elif e else

"""
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

"""
# Tabuada adição (contador)

x = 1
soma = 0 #acumulador
while x <= 10:
    n = int(input("Digite um número: "))
    soma = soma + n
    x = x + 1
print(soma)


