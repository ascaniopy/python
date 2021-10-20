galera = list()
dado = list()
totmai = totmen = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(str(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(0)
        totmai += 1
    else:
        print(0)
        totmen += 1
print('Temos {} maiores e {} menores de idade'.format(totmai, totmen))




