medida = float(input('Uma distância em metros: '))

dm = medida * 10
cm = medida * 100
mm = medida * 1000

dam = medida / 10
hm = medida / 100
km = medida / 1000

print()

print('A medida de {} m, corresponde a {:.0f} decímetros'.format(medida, dm))
print('A medida de {} m, corresponde a {:.0f} centímetros'.format(medida, cm))
print('A medida de {} m, corresponde a {:.0f} milímetros'.format(medida, mm))

print()

print('A medida de {} m, corresponde a {} decâmetros'.format(medida, dam))
print('A medida de {} m, corresponde a {} hectrômetros'.format(medida, hm))
print('A medida de {} m, corresponde a {} quilômetros'.format(medida, km))
