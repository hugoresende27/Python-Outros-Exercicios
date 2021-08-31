cores = ["Preto","Branco","Azul","Verde","Amarelo"]
#visualizar lista
print (cores)
#visualizar nr de elementos
print ("Numero de elementos",len(cores))

#somar listas
numeros = [10,20,30,40]
print ("A soma é", sum(numeros))
#o valor maximo
print ("O valor máximo é", max(numeros))
#o valor minimos
print ("O valor minimo é",min(numeros))

#visualizar o segundo elemento da lista cores
print ("Elemento na segunda posição", cores[1])
#visualizar o ultimo elemento
print ("Ultimo elemento", cores[-1])
#visualizar do 2 ao 4 elemento
print ("Do 2 ao 4",cores[1:4])

#verificar existencia de um item
if "Preto" in cores:
    print ("Sim o preto está na lista")
#alterar um valor da lista
cores [1] ="Roxo"
print (cores)

#Inserir novo elemento na lista
cores.insert(1,"Laranja")
print (cores)
#Inserir elemento no final da lista
cores.append("Cinza")
print (cores)
#Adicionar uma lista a outra (2 listas)
cores.extend(numeros)
print (cores)
numeros.extend(cores)   
print (numeros)
#remover elemento específico
cores.remove("Roxo") #remove roxo
cores.pop(5)  #remove o elemento 5
print (cores)
#eliminar elemento
del cores[5]
print (cores)
#eliminar toda a lista
#del cores
print (cores)
#esvaziar a lista
#cores.clear()
print (cores)

#percorrer lista
c=0
for x in cores:
    c+=1
    print (x,end=" || ")
print ("C:: ",c)

#ordenar a lista
cores2 = ["Preto","Branco","Azul","Verde","Amarelo","vermelho","roxo","cinza"]

cores2.sort()
print (cores2)
#no caso de maiusculas e minusculas
cores2.sort(key=str.lower)
print (cores2)
#ordenar descendente
cores2.sort(reverse=True ,key=str.lower)