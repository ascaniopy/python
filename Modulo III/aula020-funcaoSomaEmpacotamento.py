def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print('Somando os valores {} temos {}'.format(valores, s))

#Programa principal
soma(5, 9)
soma(2, 9, 4)
soma(10, 5, 25, 10, 50)
