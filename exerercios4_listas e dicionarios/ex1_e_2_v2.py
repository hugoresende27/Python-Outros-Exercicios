L=[5,7,2,9,4,1,3,5,6]

print (len(L))
print (min(L))
print (max(L))
print (sum(L))
L.sort()
print(L)
L.sort(reverse=True)
print(L)

##################### 2 ##############
nomes=[]
for x in range(5):
    nomes.append(input("Qual o nome?"))
print (nomes)
print(nomes[2])
nomes[0]="Huugo"
print (nomes)
nomes.insert(1,"Maria")
print(nomes)
nomes.pop(-1)
print(nomes)
nomes.sort()
print(nomes)