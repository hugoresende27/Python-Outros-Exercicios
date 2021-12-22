# Programa que insere numa lista 5 números inteiros pedidos ao utilizador e executa as seguintes 
# instruções:
# a. Mostrar todos os valores da lista
# b. Mostar o valor máximo e minimo
# c. Mostrar a média
# d. Mostrar os valores maiores que a média
# e. Pedir um valor ao utilizador e verifica se está na list

listaNum = []

for x in range(5):
    listaNum.append(int(input("Qual o valor? -> ")))


print (listaNum)
print("MAIOR:: ",max(listaNum))
print("MENOR:: ",min(listaNum))
media = float((sum(listaNum)/len(listaNum)))
print("MEDIA:: ",media)

print ("ACIMA DA MEDIA:: ")
for x in listaNum:
    if (x>media):
        print (x,end=" | ")
        
valor = int(input("Qual o valor? "))

if valor in listaNum:
    print ("PRESENTE")
else:
    print ("Não está! ")

