# Programa que guarda numa lista os multiplos de 3 de 1 a 50 e colocar os valores pares numa 
# nova lista. No final devem ser apresentadas as duas listas.

listaTodos = []
pares =[]
for x in range(0,50,3):
    listaTodos.append(x)
    if (x%2 ==0):
        pares.append(x)
        
        
print (listaTodos)
print (pares)