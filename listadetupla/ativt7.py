minha_tupla = ('banana', 'maçã', 'uva', 'abacaxi', 'laranja', 'morango', 'pêssego')


contador = 0


for palavra in minha_tupla:
    if len(palavra) > 5:
        contador += 1


print("Quantidade de strings com mais de 5 caracteres na tupla:", contador)