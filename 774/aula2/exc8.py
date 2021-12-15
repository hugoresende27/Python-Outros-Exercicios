#Programa que vai pedindo valores até a sua soma atingir, pelo menos, 20 valores

soma=0
while (soma<20):
    val = int (input("Qual o nr? --> "))
    soma+= val
    print ("TOTAL:: %s" %soma)

print("TERMINADO")