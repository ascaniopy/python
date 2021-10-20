def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

# Programa principal
n = int(input('Digite um número: '))
print('O fatorial de {} é igual a {}'.format(n, fatorial(n)))

print()

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print('Os resultados são: {}, {} e {}'.format(f1, f2, f3))
