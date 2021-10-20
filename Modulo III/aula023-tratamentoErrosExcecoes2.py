try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print('O erro encontrado foi {}'.format(erro.__cause__))
else:
    print('O resultado é: {:.2f}'.format(r))
finally:
    print('Volte sempre! Muito obrigado!')
