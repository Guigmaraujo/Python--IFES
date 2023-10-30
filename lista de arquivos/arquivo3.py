with open("lista de arquivos/estudantes.txt", "r") as estudantes:
    nome_para_atualizar = input("Digite o nome do estudante a ser atualizado: ")
    for estudante in estudantes:
        if estudante["nome"] == nome_para_atualizar:
            idade_nova = int(input(f"Digite a nova idade para {estudante['nome']}: "))
            curso_novo = input(f"Digite o novo curso para {estudante['nome']}: ")
            estudante["idade"] = idade_nova
            estudante["curso"] = curso_novo


with open("lista de arquivos/estudantes.txt", "w") as arquivo:
    for estudante in estudantes:
        arquivo.write(f"Nome: {estudante['nome']}, Idade: {estudante['idade']}, Curso: {estudante['curso']}\n")
