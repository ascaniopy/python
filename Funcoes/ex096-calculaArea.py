def area(larg, comp):
    a = larg * comp
    print('A área de um terreno de {:.2f} x {:.2f} é de {:.2f} m².'.format(larg, comp, a))


# Programa principal
print('{:=^55}'.format(' Controle de Terrenos '))
l = float(input('LARGURA (M): '))
c = float(input('COMPRIMENTO (M):'))
area(l, c)
print('=' * 55)

