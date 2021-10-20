while True:
    n = int(input('Quer ver tabuada de qual valor? '))
    if n < 0:
        break
    print('{:=^40}'.format(' TABUADA '))
    print('{:=^40}'.format(' DIGITE UM NÚMERO NEGATIVO PARA ENCERRAR. '))

    for c in range(1, 11):
        res = n * c
        print('{:2} x {:2} = {}'.format(n, c, res))
    print('=' * 40)
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE.')



