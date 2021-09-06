res=""
lista=[]
lista_pares=[]
lista_impares=[]

while res != "n":
    lista.append(int(input("Digite um número:: ")))
    res=input("Quer continuar? [S/N]:: ")

for index,valor in enumerate (lista):               #igual a ter for x in lista, e trabalhar com o valor x
    if valor % 2 == 0:                              #por alguma razao o prof guanabara usa o enumerate muita vez
        lista_pares.append(valor)                   #para percorrer as listas com o index e elementos respetivamente
    else:
        lista_impares.append(valor)

print ("a lista completa é :: %s" %lista)
print ("a lista de pares é :: %s" %lista_pares)
print ("a lista de impares é :: %s" %lista_impares)