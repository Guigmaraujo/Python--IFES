numero = [1, 1, 2, 4, 5, 4, 7 , 9 , 9 , 8 , 7 , 6 , 4]
reserva = []

for n in numero:
    if n not in reserva:
        reserva.append(n)
print(reserva)    