from atividade import *

notas = []


while len(notas) < 4:
    notas.append(info(nome, g1, g2))
    cont += 1
print(notas)

media = (i[1] + (i[2]*2)/3)
if media >= 6.0:
    print('Aprovado')
if media <= 6.0:
    print('Substituição')

print(i[0], i[1], i[2], media,)
