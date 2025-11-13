'''
with open ("dados.txt", "w") as arquivo:
    arquivo.write("Hugor\n")


#Ler dados
with open ("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())

#Alterar dados
with open ("dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()

#Modificar dados
with open ("dados.txt", "w") as arquivo:
    for linha in linhas:
        if linha.strip() == "Henrique":
            arquivo.write("Darlan\n")
        else:
            arquivo.write(linha)

'''

#Deletar dados
with open ("dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()

with open ("dados.txt", "w") as arquivo:
    for linha in linhas:
        if linha.strip() != "Cesar":
            arquivo.write(linha)

