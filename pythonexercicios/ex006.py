n = int(input('Digite um número: '))

dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print('O doblo de {} vale {}.'.format(n, dobro))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, triplo, n, raiz))
