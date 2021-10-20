from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('=' * 35)
    print('Contagem de {} até {} com passo {}'.format(i, f, p))
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print('{} '.format(cont), end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print('{} '.format(cont), end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')

# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('=' * 35)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
