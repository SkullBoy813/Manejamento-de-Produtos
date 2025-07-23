class Produto():
    def __init__(self, nome, preco, quantidade, categoria):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.categoria = categoria
    
    # Gets

    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco

    def get_quantidade(self):
        return self.quantidade

    def get_categoria(self):
        return self.categoria
    # Sets

    def set_nome(self, nome):
        self.nome = nome

    def set_preco(self, Preco):
        self.preco = Preco

    def set_quantidade(self, Quantidade):
        self.quantidade = Quantidade

    def set_ctegoria(self, Categoria):
        self.categoria = Categoria
   
    # Metodos

    def Detalhes(self):
        print(
            f"Produto: {self.nome} | Preço: R${self.preco:.2f} | Quantidade: {self.quantidade} | Categoria: {self.categoria}")

    def Upt_preco(self, novo_preco):
        self.preco = novo_preco

    def Upt_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade

    def desconto(self, porcentagem):
        self.preco = self.preco - self.preco * \
    porcentagem/100  # Parametos que já existem
        
    # Metodo especial para ser chamado automaticamente ao usar print()
   
    def __str__(self):
        return f"Produto: {self.nome} | Preço: R${self.preco:.2f} | Quantidade: {self.quantidade} | Categoria: {self.categoria}"