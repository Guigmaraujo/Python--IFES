
tupla = (12, 15, 8, 20, 18)

todos_maiores_que_10 = all(numero > 10 for numero in tupla)


if todos_maiores_que_10:
    print("Todos os elementos na tupla são maiores que 10.")
else:
    print("Pelo menos um elemento na tupla não é maior que 10.")
