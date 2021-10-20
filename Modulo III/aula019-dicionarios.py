pessoas = {'Nome': 'Gustavo', 'Sexo': 'M', 'Idade': 52}
print(pessoas)
print(pessoas['Nome'])
print(pessoas['Sexo'])
print(pessoas['Idade'])
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)
print()

del pessoas['Sexo']
for k in pessoas.values():
    print(k)


