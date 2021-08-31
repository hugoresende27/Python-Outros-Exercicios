lista = []

def criar_lista (valor):
    while valor != 0:
        lista.append(valor)
        valor=int(input("Qual o valor? (0 para terminar) :: "))
    return lista

def pesq_lista(x):
    if x in lista:
        return True
    else:
        return False


criar_lista(int(input("Qual o valor? (0 para terminar) :: ")))
print (lista)
pesq_lista(int(input("Qual o nr? :: ")))

     
    