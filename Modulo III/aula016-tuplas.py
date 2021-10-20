lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(len(lanche))
print()

print(lanche[0])
print(lanche[1])
print(lanche[2])
print(lanche[3])

print()

for comida in lanche:
    print('Eu vou comer {}'.format(comida))

print()

for pos, comida in enumerate(lanche):
    print('Eu vou comer {} na posição {}'.format(comida, pos))

print()

print(sorted(lanche))

print()

a = (2, 5, 4)
b = (5, 8, 1, 2)
print(a)
print(b)
c = a + b
d = b + a

print(c)
print(d)
print(c.count(5))  # Conta quantos 5 aparece na variável c.
print(c.index(8))  # A posicão do 8 na variável c.

print()

pessoa = ('Ascânio', 52, 'M', 65.7)
print(pessoa)



