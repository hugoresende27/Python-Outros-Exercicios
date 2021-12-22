#Dada a lista L=[5,7,2,9,4,1,3], escreva um programa que imprima as seguintes informações:
# a. Tamanho da lista
# b. Maior valor da lista
# c. Menor valor da lista
# d. Soma de todos os elementos da lista
# e. Lista em ordem crescente
# f. Lista em ordem decrescente

L=[5,7,2,9,4,1,3]
print("TAMANHO:: ",len(L))
print("MAIOR:: ",max(L))
print("MENOR:: ",min(L))
print("SOMA:: ",sum(L))
L.sort()
print("ORDEM NORMAL:: ",L)
L.sort(reverse=True)
print("ORDEM REVERSE:: ",L)