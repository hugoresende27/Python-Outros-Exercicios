##############################################
#################   listas    ################
cores=["preto","branco","verde","amarelo","azul"]   

print(cores)                                                        #visualizar lista

print("Número de elementos da lista cores:",len(cores))             #Visualizar número de elementos
numeros=[10,20,30,40]

print("Soma dos valores da lista números:",sum(numeros))            #Aplicar funções a listas

print("Elmento na segunda posição da lista cores:",cores[1])        #Visualizar o segundo elemento da lista cores

print("Último elemento da lista cores é",cores[-1])                 #Visualizar o último elemento da lista

print(cores[1:3])                                       #Utilizar gamas de índices

if "verde" in cores:                                    #Testar se ver está na lista cores
    print("O verde está presente na lista!")       

cores[1]="castanho"                                     #Alterar de branco para castanho
print(cores)

cores.insert(1,"laranja")                               #Inserir novo elemeto na lista no indice 1
print(cores)

cores.append("cinza")                                   #Inserir elemento no final da lista
print(cores)

cores.extend(numeros)                                   #Adicionar duas listas
print(cores)

cores.remove("amarelo")                                 #Remover elemento através de conteudo

cores.pop(0)                                            #Remover atravé de índice
print(cores)

for x in cores:                                         #Percorrer lista
    print(x)

#cores.sort()                                           #Ordenar lista de forma ascendente
print(cores)

numeros.sort(reverse=True)                              #Ordenar lista de forma descendente
print(numeros)