
def soma1(a,b):
    print(a+b)
def soma2(a,b):
    return a+b


#Erros:
#def soma2(a,b):
#    return print(a+b)
#def soma2(a,b):
#    resp = a+b


def soma (*a):
    acum = 0
    for i in a:
        acum+=i
    return acum
