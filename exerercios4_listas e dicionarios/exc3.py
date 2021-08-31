
multiplos3=[]
pares =[]
pares2=[]

for x in range (1,51): 
    if x%3 == 0:
        multiplos3.append (x)
        if x%2 == 0:
            pares.append(x)
       

print ("Multiplos de 3 de 1 a 50 ::" ,multiplos3)
print ("Pares multiplos de 3 de 1 a 50 ::" ,pares)

###########outra solução ####

for y in range(len(multiplos3)):        #percorrer a lista multiplos3
    if multiplos3[y]%2 == 0:
        pares2.append(multiplos3[y])

print("Outra solucao::",pares2)
