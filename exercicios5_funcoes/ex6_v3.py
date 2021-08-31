def pesquisar (l,valor):
    if valor in l:
        return True
    else:
        return False

lista =[1,2,3,4]
n=int(input("Valor a pesquisar :: "))
if (pesquisar(lista,n)):                        #(pesquisar(lista,n))==True era igual
    print ("o valor %s está presente na lista" %n)
else:
    print ("o valor %s NÂO está presente na lista" %n)