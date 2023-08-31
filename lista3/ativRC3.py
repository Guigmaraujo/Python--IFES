import random

ns = random.randint(1,100)

while True:
    t = int(input('Digite um número: '))


    if t ==ns:
        print('Você acertou o número secreto!')
        break
    elif t<ns:
        print(f'Tente um número maior que: {t} ')
    else:
        print(f'tente um número menor que: {t} ')