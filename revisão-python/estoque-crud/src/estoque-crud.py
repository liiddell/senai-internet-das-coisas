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
    with open("estoque.txt", "r") as arquivo:



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
        elif opcao == "5":
            break
        else:
            print("Opção invalida!")


menu()