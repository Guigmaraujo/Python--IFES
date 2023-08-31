x = int(input('Digite o x: '))
y = int(input('Digite o y: '))

if x > 0 and y > 0:
    print(f'As coordenadas {x} e {y} estão no primeiro quadrante!')
elif x < 0 and y > 0:
    print(f'As coordenadas {x} e {y} estão no segundo quadrante!')
elif x < 0 and y < 0:
    print(f'As coordenadas {x} e {y} estão no terceiro quadrante!')
else:
    print(f'As coordenadas {x} e {y} estão no quarto quadrante!')