

cores=["preto","branco","verde","amarelo","azul"]
#visualizar lista
print(cores)
#Visualizar número de elementos
print("Número de elementos da lista cores:",len(cores))
numeros=[10,20,30,40]
#Aplicar funções a listas
print("Soma dos valores da lista números:",sum(numeros))
#Visualizar o segundo elemento da lista cores
print("Elmento na segunda posição da lista cores:",cores[1])
#Visualizar o último elemento da lista
print("Último elemento da lista cores é",cores[-1])
#Utilizar gamas de índices
print(cores[1:3])
#Testar se ver está na lista cores
if "verde" in cores:
    print("O verde está presente na lista!")
#Alterar de branco para castanho
cores[1]="castanho"
print(cores)
#Inserir novo elemeto na lista no indice 1
cores.insert(1,"laranja")
print(cores)
#Inserir elemento no final da lista
cores.append("cinza")
print(cores)
#Adicionar duas listas
#cores.extend(numeros)
#print(cores)
#Remover elemento através de conteudo
cores.remove("amarelo")
#Remover atravé de índice
cores.pop(0)
print(cores)
#Percorrer lista
for x in cores:
    print(x)
#Ordenar lista de forma ascendente
cores.sort()
print(cores)
#Ordenar lista de forma descendente
numeros.sort(reverse=True)
print(numeros)