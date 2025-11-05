
print("Teste")

num1 = 10
num2 = 20

#Operações

#soma
print(num1 + num2)
resultado = num1 + num2
print(resultado)

#subtração
print(num1 - num2)

#multiplicação
print(num1 * num2)

#divisão
print(num1 / num2)

#módulo
print(num1 % 2)


#Saída de dados

nome = "Hospitalina"
idade = 50
peso = 55.3

print("Dados da pessoa:")
#Forma antiga
print("%s tem %d anos e pesa %.1f kg" % (nome, idade, peso))
print("----------------------------------------")
#Forma nova
print("{} tem {} anos e pesa {} kg.".format(nome, idade, peso))
print("----------------------------------------")
#Forma nova da nova
print(f"{nome} tem {idade} anos e pesa {peso} kg.")
print("----------------------------------------")

#Entrada de dados
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
peso = input("Digite seu peso: ")

print("----------------------------------------")
print("{} tem {} anos e pesa {} kg.".format(nome, idade, peso))
print("----------------------------------------")

#Estruturas condicionais

numero = int(input("Digite um numero: "))
if numero > 0:
    print("Este número é positivo!")
elif numero < 0:
    print("Este número é negativo!")
else:
    print("O número é 0!")
