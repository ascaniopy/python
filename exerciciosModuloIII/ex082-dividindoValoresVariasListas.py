num = list()
pares = list()
impares = list()

while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))

    if resp in 'Nn':
        break

for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('=' * 30)
print('A lista completa é {}'.format(num))
print('A lista de pares é {}'.format(pares))
print('A lista de ímpares é {}'.format(impares))
print('=' * 30)
