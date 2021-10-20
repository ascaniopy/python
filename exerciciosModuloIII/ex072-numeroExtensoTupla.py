cont = ('zero', 'um', 'dois', 'três', 'quatro')
while True:
    num = int(input('Digite um número entre o e quatro: '))
    if 0 <= num <= 4:
        break
    print('Tente novamente. ', end='')
print('Você digitou o número {}'.format(cont[num]))



