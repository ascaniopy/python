def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

#Programa principal

valores = [6, 13, 9, 1, 0, 2]
dobra(valores)
print(valores)

