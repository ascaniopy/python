print('='*50)
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(s, m, d))
print('Divisão inteira = {} e potência = {}'.format(di, p))
print('='*50)