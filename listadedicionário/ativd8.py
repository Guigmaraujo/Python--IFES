cnts = {'Guilherme': "99257-5062", 'Pedro' : '99858-8151', 'José Augusto': "99705-7063"}
nar = 'Guilherme'
if nar in cnts:
    del cnts[nar]
for i,n in cnts.items():
    print(f'O Nome é: {i}, O número é: {n}')