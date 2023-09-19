
t1 = (1, 2, 3)
t2 = (4, 5, 6)


tupla_soma = tuple(x + y for x, y in zip(t1, t2))


print(f"Tupla 1:{t1}")
print(f"Tupla 2:{t2}")
print("Tupla com a soma dos elementos correspondentes:", tupla_soma)
