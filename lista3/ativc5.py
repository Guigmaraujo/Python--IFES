l1 = float(input('Digite o l1 de um triângulo: '))
l2 = float(input('Digite o l2 de um triângulo: '))
l3 = float(input('Digite o l3 de um triângulo: '))

if l1==l2==l3:
    print('O triângulo é equilátero!')
elif l1==l2 or l2==l3 or l1==l3:
    print('O triângulo é isósceles!')
else:
    print('O triângulo é escaleno!')