# Dadas as listas L1=[5,7,2,9,4] e L2=[1,8,5,3,2], crie um programa que soma os valores por 
# indice e coloca o resultado numa nova lista. A nova lista deve ser apresentada por ordem 
# crescente. O programa também deve permitir saber quantos elementos tem em comum.

L1=[5,7,2,69,9,4,89]
L2=[1,8,5,3,2,69,55]
L3 = []

for x in range(len(L1)):
   L3.append(L1[x]+L2[x])

print (L3)
L3.sort()
print (L3)

contar = 0
for x in L1:
   for y in L2:
          if x == y:
            contar+=1
            print (x,end=" - ")   
print ("Elementos em comum: ",contar)


L4 = []
L4=[x + y for x, y in zip(L1, L2)]
print(L4)
