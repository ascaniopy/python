def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

# Programa principal
num = int(input('Digite um número: '))
if par(num):
    print('É PAR.')
else:
    print('NÃO É PAR.')
