from math import radians, sin, cos, tan

angulo = float(input('digite o ângulo: '))

seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.4f}'.format(angulo, seno))

cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSENO de {:.4f}'.format(angulo, cosseno))

tangente = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.4f}'.format(angulo, tangente))
