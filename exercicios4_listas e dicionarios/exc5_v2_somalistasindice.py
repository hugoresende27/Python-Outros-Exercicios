L1=[5,7,2,9,4]
L2=[1,8,5,3,2]
novalista=[]
contar=0
for x in range(5):
    novalista.append(L1[x]+L2[x])       ###somar listas com ciclo for
    
print (novalista)
novalista.sort()
print (novalista)

for i in L1:
    for j in L2:
        if i ==j : contar+=1
       # if L1[i] == L2[j]:
print ("Iguais", contar)
