alimentos = {
    'Maça' : 13000,
    'Banana' : 1000,
    'Abacate' : 500,
}

calorias_consumidas = 0

while True:
    come = input("Digite o nome do alimento consumido ou '0' para parar: ")

    if come == '0':
        break
    else:
        for alimento in alimentos.items():
            if alimento[0] == come:
                calorias_consumidas+=alimento[1]

print(f"O total de calorias Consumidas foram: {calorias_consumidas}")