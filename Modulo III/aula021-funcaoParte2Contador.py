def contador(i, f, p):
    """
    -> Faz uma contaem e mostra na tela.
    :param i: início da contagem.
    :param f: fim da contagem.
    :param p: passo da contagem.
    :return: sem retorno.
    """

    c = 1
    while c <= f:
        print('{}'.format(c), end=' ')
        c += p
    print('FIM!')

#Prorama principal
contador(0, 71, 7)




