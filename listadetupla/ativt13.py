
minha_tupla = (3, 4, 6, 8, 10)


todos_pares = True


for n in minha_tupla:
    if n % 2 != 0:
        todos_pares = False
        break


if todos_pares:
    print("Todos os elementos na tupla são pares.")
else:
    print("Pelo menos um elemento na tupla não é par.")
