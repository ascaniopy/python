def somar(a=0, b=0, c=0):

    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor.
    :param b: o segundo valor.
    :param c: o terceiro valor.
    :return: sem retorno.
    """
    s = a+ b + c
    print('A soma vale: {}'.format(s))

# Prorama principal
somar()
somar(0)
somar(3)
somar(3, 2)
somar(3, 2, 5)
somar(b=4, c=10)

