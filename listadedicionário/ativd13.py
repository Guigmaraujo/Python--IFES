estoque_produtos = {
    'Maçãs': 50,
    'Bananas': 30,
    'Laranjas': 10,
    'Pêras': 25
}

estoque_minimo = 20
produtos_com_baixo_estoque = {produto: estoque for produto, estoque in estoque_produtos.items() if estoque < estoque_minimo}
print(produtos_com_baixo_estoque)
