lista=[]
for x in range (4):
    lista.append (input("Qual o nome? "))
    
print ("a. Lista::",lista)
print ("b. Nome posição 3",lista[2])
lista[0]="Hugo"
print ("c. ",lista)
lista.insert(1,"Maria")
print ("d. ",lista)
lista.pop(-1)
print ("e. ", lista)
lista.sort(key=str.lower)
print (lista)



  