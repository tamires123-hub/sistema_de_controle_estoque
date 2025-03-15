from datetime import datetime

lista_de_produtos = []
estoque = []

def cadastrar(id: int, nome: str, categoria: str, quantidade: int, preco: int, dt_validade: None):
   validade = datetime.strptime(dt_validade, "%d/%m/%Y").date()
   produto = {
    "ID" : id, 
    "Nome" : nome, 
    "Categoria" : categoria,
    "Quantidade" : quantidade, 
    "Preço" : preco, 
    "Validade" : validade,
    "Disponível para venda" : True if validade is None or validade > datetime.today().date() else False
    }
    lista_de_produtos.append(produto)

def adicionar_produto(id: int, quantidade: int):
    for produto in estoque:
        if produto["id"] == id:
            produto["quantidade"] += quantidade
            return
    print("Produto não encontrado.")

def remover_produto(id: int, quantidade: int):