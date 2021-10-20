palavras = ('aprender', 'programar', 'linguagem', 'python')

for p in palavras:
    print('\nNa palavra {}, temos: '.format(p.upper(), p), end='')

    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

