print("\n\t\t Bem vindo ao aplicativo de Compras\n")

#Declaração de variaveis
continuar = "S"
escolha:int
listaDeCompras = []

#Função para imprimir lista
def listaItens():
    contador = 1
    print("\n\tLista de itens")
    for item in listaDeCompras:
        print(f"\t{contador}º {item}")
        contador += 1
    print()

#Processamento de dados
while True:
    try:
        escolha = int(input("\t[1] -> Adicionar\n\t[2] -> Remover\n\t[3] -> Sair\n\tResposta: "))
        if escolha < 1 or escolha > 3:
            raise ValueError
        
        if escolha == 1:
            num = int(input("Quantos itens deseja adicionar? "))
            for i in range(num):
                item = input(f"Digite o item {i+1}: ")
                listaDeCompras.append(item)
                print(f"Adicionado {item} com sucesso.")
        elif escolha == 2:
            #For para remover item verificar se item existe
            if len(listaDeCompras) == 0:
                print("Não há nenhum item na lista.")
            else:
                listaItens()
                item = input("Qual item deseja remover?")
                if item in listaDeCompras:
                    listaDeCompras.remove(item)
                    print(f" Item {item} removido com sucesso.")
                else:
                    print("Item não existe na lista.")
                listaItens()
        else: 
            print("Programa encerrando.")
            break

        
    except:
        print("ERRO! Digite um valor correto.")
print("\nObrigado por utilizar o aplicativo.\nSegue lista de compras atualizada")
listaItens()