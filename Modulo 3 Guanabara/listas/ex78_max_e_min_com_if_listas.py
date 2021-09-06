valores=[]      
mai=men=0           #inicializar var maior e menor a 0

for x in range (5):
    valores.append(int(input("Digite um valor para a posição %s :: " %x)))      #adicionar 5 elementos a uma lista
    if x == 0:                      #quando o index for 0, ou seja o primeiro
        mai=men=valores[x]          #maior e menor e elementos tudo é igual a 0
    else:                           #quando o index passa a ser 1, ou seja depois do primeiro input
        if valores[x]>mai:          #se elemento do input [x]>maior, 0 no primeiro ciclo, passa a ser o maior
            mai=valores[x]      
        if valores[x]<men:         #se for menor q o valor, passa a ser o menor, neste caso o primeiro     
            men=valores[x]          #valor introduzido vai ser o maior e o menor
    

print ("Você digitou os valores :: " ,valores)

print ("O maior valor digitado foi o %s na posição index" %mai,end=" ::"  )
for index,valor in enumerate (valores):     #precorrer lista com index e elementos, com o enumerate
    if valor == mai:                        #quando o elemento for igual ao maior
        print (index)                       #dá print no index

print ("O menor valor digitado foi o %s na posição index" %men,end=" :: " ) 
for index, valor in enumerate(valores):        #igual mas para o menor
    if valor == men:
        print (index) 