#Revisão de listas e funções das listas
'''
#Exemplo básico de lista

z = [1,2,3,4,5]
print(z)
print(z[0])
print(z[1])
print(z[2])

lista = [1,2,3,4,5,6]
print(len(lista))
#Adiciona
lista.append(7)
print(lista)
#Remove o elemento
lista.remove(2)
print(lista)
#Remove o indice
lista.pop(3)
print(lista)
#Remove elemento pelo indice
del lista[0]
print(lista)


# Buscar elemento dentro da lista
lista = [1,2,3,4,5,6]
num = int(input("Digite um número: "))
if num in lista:
    print("O número está na lista!")
else:
    print("O Número não existe")

'''