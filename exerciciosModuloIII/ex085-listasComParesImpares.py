num = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input('Digite o {}º valor: '.format(c)))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('=' * 50)
num[0].sort()
num[1].sort()
print('Os valores pares digitados foram: {}'.format(num[0]))
print('Os valores ímpares digitados foram: {}'.format(num[1]))
print('=' * 50)
