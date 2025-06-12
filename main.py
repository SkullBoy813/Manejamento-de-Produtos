from Produtos import Produto


produtos = [] # Fora do while true
def buscar_produto(nome_busca, lista_produtos):
    for produto in lista_produtos:
        if produto.nome.lower() == nome_busca.lower():
            return produto
      
while True:

    print("\n====Menu do Sistema====")
    print("[1]Cadastrar produto")
    print("[2]Listar os produtos")
    print("[3]Atualizar Preço")
    print("[4]Atualizar Quantidade")
    print("[5]Aplicar desconto")
    print("Qual a opção desejada?")
    selecionador = int(input())

    if selecionador == 1:
        print("\n===Cadastro do Produto===")
        print("Insira o nome do seu produto:")
        nome_classe = str(input())
        print("Insira o preço do seu produto:")
        preco = int(input())
        print("Insira a quantidade do seu produto:")
        quantidade = int(input())
        print("Insira a categoria do seu produto:")
        categoria = str(input())
        nome_classe = Produto(nome_classe, preco, quantidade, categoria)
        produtos.append(nome_classe)
        print("Produto criado com sucesso!\n")

    elif selecionador == 2:
        print("\n===lista dos seus Produtos===")
        # Para o i(numerador), o produto em inumerador(produto):
        for i, produto in enumerate(produtos):
            print(f"[{i}] {produto}")

    elif selecionador == 3:
        print("\n===Atualizador de preço===")
        print("Qual produto você deseja atualizar?")
        nome_busca = str(input())
        encontrado = buscar_produto(nome_busca, produtos)
        if encontrado:
             print("!!!Produto encontrado!!!")
             print("Qual sera o novo preço?")
             dado = int(input())
             nome_classe.Upt_preco(dado)
             print(f'O preço do produto {nome_busca} foi atualizada para:{nome_classe.get_preco()}')
        else:
            print("Produto não encontrado")            

    elif selecionador == 4:
        print("\n===Atualizador de Quantidade===")
        print("Qual produto você deseja atualizar?")
        nome_busca = str(input())
        encontrado = buscar_produto(nome_busca, produtos)#a função ira ser usada dentro de uma variavel para verificar se existe ou não
        if encontrado:
             print("!!!Produto encontrado!!!")
             print("Qual sera a nova quantidade do produto?")
             dado = int(input())
             encontrado.Upt_quantidade(dado)
             print(f'A quantidade do produto {nome_busca} foi atualizada para {encontrado.get_quantidade()}')
        else:
            print("Produto não encontrado")
              
    elif selecionador == 5:
        print("\n===Aplicar o desconto===")
        print("Em qual protudo você deseja aplicar o desconto?")
        nome_busca = str(input())
        encontrado = buscar_produto(nome_busca, produtos)
        if encontrado:
            print("!!!Produto encontrado!!!")
            desconto = int(input("Quanto sera o desconto adicionado ao produto?"))
            nome_classe.desconto(desconto)
            nome_classe.Detalhes()
        else:
            print("Produto não encontrado")
        

