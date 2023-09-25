pp = {"arroz":9, "maça":4, "banana":2}
lista = ["arroz", "maça", "banana"]
t = sum(pp[produto] for produto in lista)
print(f'O total da compra deu: {t}')