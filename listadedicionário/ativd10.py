dicionario_definicoes = {
    'Python': 'Uma linguagem de programação de alto nível.',
    'Internet': 'A rede global de computadores.',
    'Dicionário': 'Uma coleção de pares chave-valor.'
}

palavra_chave = input('Digite a palavra-chave: ')
if palavra_chave in dicionario_definicoes:
    print(dicionario_definicoes[palavra_chave])
else:
    print('Palavra-chave não encontrada.')
