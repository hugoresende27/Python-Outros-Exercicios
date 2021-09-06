
from random import randint
from time import sleep



def sorteia():
    for x in range(5):
        lista.append(randint(1,10))
    print ("Sorteando os valores da lista:", end=" ")
    for x in lista:
        print (x,end=" ",flush=True)
        sleep(0.3)
    print ("PRONTO!")

def somaPar (valores):            
    s=0                         #soma a 0
    for num in lista:                   #basta um ciclo for para correr a lista, se for par print,
        if num % 2 == 0:                #não preciso de outra lista
            s+=num                  #soma os valores
    print ("Somando os valores pares temos %s" %s) 

def sorteia2 ():
    print ("Sorteando os valores da lista:", end=" ")
    for n in range (5):             
        n=randint(1,10)
        lista.append(n)
        print (n,end=" ",flush=True)
        sleep(0.3)
    print ("PRONTO!")


lista=list()


sorteia2()
somaPar(lista)

