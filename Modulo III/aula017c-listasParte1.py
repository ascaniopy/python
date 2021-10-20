a = [2, 3, 4, 7]
b = a                 # Aqui troca nas duaas listas.
b[2] = 8
print('Lista A:', a)
print('Lista B:', b)

print()
print()

a = [2, 3, 4, 7]
b = a[:]               # Aqui troca só na lista B.
b[2] = 8
print('Lista A:', a)
print('Lista B:', b)



