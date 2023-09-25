cnts = {'Guilherme': "99257-5062", 'Pedro' : '99858-8151', 'José Augusto': "99705-7063"}
n_ctt = {'Enzo': '99769-2315'}
cnts.update(n_ctt)
for i,n in cnts.items():
    print(f"O nome é: {i}, o número é: {n}")