print('{:=^70}'.format('DIGITA NÚMEROS, CONTA PARES E ÍMPARES E PARA COM 0.'))
n = 1
par = impar = 0
while n != 0:
    n = int(input('digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))




