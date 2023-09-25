paises_capitais = {
    'Brasil': 'Brasília',
    'EUA': 'Washington, D.C.',
    'França': 'Paris'
}

pais = input('Digite o nome do país: ')
if pais in paises_capitais:
    print(f'A capital de {pais} é {paises_capitais[pais]}.')
else:
    print('País não encontrado.')
