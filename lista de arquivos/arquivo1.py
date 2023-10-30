
estudantes = []


while True:
    nome = input("Digite o nome do estudante (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    idade = int(input("Digite a idade do estudante: "))
    curso = input("Digite o curso do estudante: ")
    estudante = {"nome": nome, "idade": idade, "curso": curso}
    estudantes.append(estudante)


with open("estudantes.txt", "w") as arquivo:
    for estudante in estudantes:
        arquivo.write(f"Nome: {estudante['nome']}, Idade: {estudante['idade']}, Curso: {estudante['curso']}\n")
