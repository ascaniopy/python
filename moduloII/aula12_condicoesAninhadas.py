nome = str(input('Qual o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Juliana Jéssica':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))