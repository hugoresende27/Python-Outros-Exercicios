L1=[12,33,44,55,66,77,99,100]
L2=[1 ,2 ,3 ,100 ,5 ,77 ,7 ,8 ]
L3=[]

print (len(L1))
comp = len(L1)
for x in range (comp):
        L3.append(L1[x]+L2[x])

print (L3)

contar=0
for x in L1:
        for y in L2:
                if x==y:
                        print("elementos iguais::", x)
                        contar+=1
print ("existem %d elementos iguais"%contar)