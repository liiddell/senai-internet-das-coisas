# Entradas manuais

def adicionar_item():
    codigo = input("Código: ")
    descricao = input("Descrição: ")
    fabricante = input("Fabricante: ")
    quantidade = int (input("Quantidade: "))
    preco = float(input("Preço: "))


    with open("estoque.txt", "w") as arquivo:
        arquivo.write(f'{codigo}, {descricao}, {fabricante}, {quantidade}, {preco}\n')
    print("Item adicionado com sucesso!")


def listar_item():
    with open("estoque.txt", "r") as arquivo:
        for linha in arquivo:
            item = linha.strip().split(",")
            print(f"Código: {item[0]} | Descrição: {item[1]} | Fabricante: {item[2]} | Quantidade: {item[3]} | Preço: {item[4]}")

def atualizar_item():
    codigo = input("Digite o código do item que deseja atualizar: ")

    with open("estoque.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("estoque.txt", "w") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] == codigo:
                print("Item encontrado, digite os novos dados: ")
                nova_descricao = input("Nova descrição: ")
                nova_fabricante = input("Nova fabricante: ")
                nova_quantidade = int (input("Nova quantidade: "))
                novo_preco = float (input("Novo preço:"))
                arquivo.write(f" {codigo}, {nova_descricao}, {nova_fabricante}, {nova_quantidade}, {novo_preco}\n")
                print("Item alterado com sucesso!")
            else:
                arquivo.write(linha)

def menu():
    while True:
        print("\n-- MENU ESTOQUE --\n")
        print(" 1 - Adicionar Item")
        print(" 2 - Listar Item")
        print(" 3 - Atualizar Item")
        print(" 4 - Excluir Item")
        print(" 5 - Sair")

        opcao = input("Escolha uma opcão: ")
        if opcao == "1":
            adicionar_item()
        elif opcao == "2":
            listar_item()
        elif opcao == "3":
            atualizar_item()
        elif opcao == "5":
            break
        else:
            print("Opção invalida!")


menu()