num = [2, 5, 9, 1]
print(num)

num[2] = 3
print(num)


num.append(7)
print(num)

num.sort()
print(num)

num.sort(reverse=True)
print(num)

num.insert(2, 0)        # Na posição 2, colocar 0.
print(num)

num.pop(0)              # Tira o número na posição 0. O número 7.
print(num)

num.remove(2)           # Tira o número 2 da lista.
print(num)

if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.')
print('Essa lista tem {} elementos.'.format(len(num)))




