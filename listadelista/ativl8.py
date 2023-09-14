ln = [0 , 12, 56, 78, 89, 16, 23, 345, 786, 456, 234, 765]

ma = 0 
me = ln[0]

for i in ln:
    if i > ma:
        ma = i

    if i < me:
        me = i

print(f'O maior número é: {ma}')
print(f'O mmenor número é: {me}')