numeros=[]
cont=0
for x in range(5):
    numeros.append(int(input("Insira um valor inteiro :: ")))
    cont+=1

print (numeros)
print (" O MAX %d e o MIN %d" %(max(numeros),min(numeros)))     #maximo e minimo
print ("MEDIA %f" %(sum(numeros)/len(numeros)))                 #media da lista
media = sum(numeros)/len(numeros)
for x in numeros:
    if x>media:
        print("MEDIA maiores do que %d::"%x)       #valores acima da média

valor=int(input("VALOR A VERIFICAR :: "))
if  valor in numeros:
    print ("SIM")
else:
    print("NAO")
