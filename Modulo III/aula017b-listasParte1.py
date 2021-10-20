valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(v, end=' ')
print()

for c, v in enumerate(valores):
    print('Na posição {} encontrei o valor {}!'.format(c, v))
print('Cheguei ao final da lista.')

print()
print()

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print('Na posição {} encontrei o valor {}!'.format(c, v))
print('Cheguei ao final da lista.')




