estoque = [20, 15, 10, 30, 5]

def atualizar_estoque(estoque, produto, quantidade): 
    """Atualiza a quantidade em estoque após uma venda."""
    if 0 <= produto < len(estoque):
        if estoque[produto] >= quantidade: 
            estoque[produto] -= quantidade
        else: 
            print(f"Não há estoque suficiente para o produto {produto + 1}.")

    else: 
        print("Produto inválido")

def adicionar_estoque(estoque, produto, quantidade):
    """Adicionar unidades de um produto ao estoque."""
    if 0 <= produto < len(estoque):
        estoque[produto] += quantidade 
    else: 
        print("Produto inválido") 

def exibir_estoque(estoque):
    """Exibe a quantidade atual de cada produto."""
    for i, quantidade in enumerate(estoque):
        print(f"Produto {i + 1}: {quantidade} unidades")


# Atualizar o estoque 
atualizar_estoque(estoque, 0, 3) # Vender 3 unidades do produto 1
atualizar_estoque(estoque, 3, 2) # Vender 2 unidades do produto 4             
