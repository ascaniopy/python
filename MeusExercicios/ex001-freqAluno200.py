print('{:=^50}'.format(' FREQUÊNCIA DO ALUNO COM 200 AULAS '))
faltas = int(input('Digite o número de faltas: '))

freq = ((200 - faltas) * 100) / 200

print('A frequência é {:.2f}%'.format(freq))

