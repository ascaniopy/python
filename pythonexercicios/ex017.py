print('======== Calcular Hipotenusa ========')

from math import hypot
cateto1 = float(input('Digite o comprimento do primeiro cateto: '))
cateto2 = float(input('Digite o comprimento do segundo cateto: '))
#hip = (cateto1 ** 2 + cateto2 ** 2) ** (1/2)
hip = hypot(cateto1, cateto2)
print('A hipotenusa vai medir {:.2f}'.format(hip))
