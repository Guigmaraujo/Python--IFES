frutas_quantidades = {
    'Maçãs': 50,
    'Bananas': 30,
    'Laranjas': 60,
    'Pêras': 40
}

fruta_mais_quantidade = max(frutas_quantidades, key=frutas_quantidades.get)
print(f'A fruta com a maior quantidade é {fruta_mais_quantidade}.')
