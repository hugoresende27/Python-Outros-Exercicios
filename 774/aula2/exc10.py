#Programa que soma apenas os números pares inseridos pelo utilizador. No final o programa 
#mostra o resultado da soma e o número de valores inseridos pelo utilizador quando for inserido 
#um valor negativo. O valor negativo não é contabilizado

soma=0
num=0
valores=-1
while (num>=0):
    num=int(input("VAL--> "))
    valores+=1
    if (num % 2 == 0):
        soma += num
        
print ("SOMA %s" %soma)
print ("TOTAL %s" %valores)

    