
#JOIN
nome = 'Joaquim Felipe Souza'
lista = nome.split(' ') # Split significa 'fatear'
print(lista) # Pra pegar o ultimo nome eu posso usar split e pegar na lista no o i[-1]

lista.pop()

x = ' antes de '
novo = x.join(lista) # ao terminar uma string ele inicia o que esta na variavel e depois continua ate a lista acabar.
print(novo)


#SPLIT
cpf = '111.222.333-44'
lista = cpf.split('-')
print(lista)

lista = cpf.split('.')
print(lista)



texto = 'a arara ara a arraia'
lista = texto.split('ar')
print(lista)
