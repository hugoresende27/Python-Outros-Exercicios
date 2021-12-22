# Programa insere numa lista 4 nomes pedidos ao utilizador e executa as seguintes instruções:
# a. Mostrar da lista
# b. Mostrar o nome da posição 3
# c. Alterar o valor do primeiro elemento da lista e apresentar o resultado
# d. Adicionar o nome “Maria” à segunda posição da lista e mostrar o resultado
# e. Remover o último elemento da lista e mostrar o resultado
# f. Apresentar a lista por ordem crescent

lista = []
for i in range(4):
    lista.append(input("Qual o nome? "))

print ("TODOS OS ELEMENTOS",lista) 
print ("Terceira Posição:: ",lista[2])
lista[0]="NomeAlterado"
print ("PRIMEIRO ALTERADO",lista)
lista.insert(1,"Maria")
print ("MARIA ADICIONADA",lista)
lista.pop(-1)
print ("ULTIMOS REMOVIDO",lista)
lista.sort(key=str.lower)
print ("ORDEM CRESCENTE",lista)

