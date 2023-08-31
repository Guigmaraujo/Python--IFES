n1 = float(input('digite um número para ver se é positivo negativo ou zero: '))

if n1>0:
    print(f'O número {n1} é positivo!'.replace('.',','))
elif n1<0:
    print(f'O número {n1} é negativo!'.replace('.',','))
else:
    print(f'O número {n1} é igual a 0!'.replace('.',','))