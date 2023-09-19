
paises_populacao = (('Brasil', 211000000), ('EUA', 331000000), ('Índia', 1380000000), ('China', 1440000000))


pais_mais_populoso = max(paises_populacao, key=lambda x: x[1])


print(f"O país mais populoso é {pais_mais_populoso[0]} com uma população de {pais_mais_populoso[1]} habitantes.")
