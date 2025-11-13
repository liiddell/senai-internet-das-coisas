# Manipulação de arquivos

# Gravando arquivo
arquivo = open('numero.txt', 'w') #Write
for linha in range(1, 101):
    arquivo.write(f'{linha}\n')
arquivo.close()

# Leitura de arquivo
arquivo = open('numero.txt', 'r')
for linha in arquivo.readlines():
    print(linha)
arquivo.close()