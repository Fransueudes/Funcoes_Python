
def ultimo(nome):
    lista = nome.split(' ')
    lista.remove('da')
    lista1 = lista[1].upper(),lista[0][0]
    juncao = ' , '
    lista2 = juncao.join(lista1)
    return lista2

def penultimo(nome):
    lista = nome.split(' ')
    lista.remove('da')
    lista1 = lista[1].upper(),lista[2].upper(), lista[0][0]
    juncao = ' '
    lista2 = juncao.join(lista1)
    return lista2



def junior(nome):
    if nome == 'Junior' or 'Filho' or 'Sobrinho' or 'Neto':
        print('True')
    else:
        print('False')
    


'''
def ponto(nome):




def divide(nome):'''


'''

lista=['A','B','C']
juncao = ' depois de '
novaString = juncao.join(lista)
print("Lista =", lista)
print("Texto =", novaString)
'''
