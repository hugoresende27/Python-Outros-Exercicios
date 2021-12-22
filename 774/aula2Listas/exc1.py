#Programa que calcula a soma da sequência seguinte.
#soma=1+4+7+10+13+16+19
print(1+4+7+10+13+16+19)
soma=0
for x in range(1,20,3):
    soma+=x
    print(x,end=" + ")
print (soma)