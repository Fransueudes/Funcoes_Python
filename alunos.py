
def lenome ():
    return input('Digite o nome: ')

def lenota ():
    return float(input('Digite a nota: '))

def media (a, b):
    return (a + (b*2))/3

def situacao (a, b):
    if b >= 6.0:
        print('O aluno', a, 'passou com media', round(b,1))
    elif b <= 6.0:
        print('O aluno', a, 'reprovou com media', round(b,1))
    
