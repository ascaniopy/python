print('{:=^40}'.format(' PA COM WHILE '))
print('{:=^40}'.format(' DIGITE 0 PARA FINALIZAR! '))
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont =1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} '.format(termo), end='')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('PA finalizada  com {} TERMOS mostrados.'.format(total))
print('{:=^40}'.format(' FIM '))




