try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print('O problema encontrado foi {}'.format(erro.__class__))
else:
    print('O resultado é: {:.2f}'.format(r))
finally:
    print('Volte sempre! Muito obrigado!')