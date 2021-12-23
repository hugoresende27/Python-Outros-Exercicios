L1=[5,7,2,9,4]
L2=[1,8,5,3,2]

L3=[x + y for x, y in zip(L1, L2)]
print (L1,L2)
print ("Soma das listas por indice ::" ,L3)
L3.sort()
print ("L3 ordenada ::",L3)


from collections import Counter
 
d = Counter(L3)
#print(d)
new_list = list([item for item in d if d[item]>1])
print("Valores em comum na lista::",new_list)