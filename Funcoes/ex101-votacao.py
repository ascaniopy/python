def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return 'Com {} anos: NÃO VOTA.'.format(idade)
    elif 16 <= idade < 18 or idade > 65:
        return 'Com {} anos: VOTO OPCIONAL.'.format(idade)
    else:
        return 'Com {} anos: VOTO OBRIGATÓRIO.'.format(idade)


# Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
