n1=int(input("NR1--> "))
n2=int(input("NR2--> "))
n3=int(input("NR3--> "))

menor = n1                  #teste do menor, atribui n1 como o menor,
if n2<n1 and n2<n3:         #testa n2 se menor ,
    menor = n2              #n2 fica o menor
if n3<n1 and n3<n2:         #testa o n3
    menor = n3              #se for menor, menor n3

maior = n1              #teste maior
if n2>n1 and  n2>n3:    #mesma lógica
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print ("O menor valor digitado foi {}".format(menor))
print ("O maior valor digitado foi {}".format(maior))