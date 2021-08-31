lista =[1,2,3,4,5,6,7,8,9]

def pesquisar(x):
    if x in lista:
        return True
    else:
        return False

valor = int(input("Qual o valor a pesquisar?? :: "))
print (pesquisar(valor))