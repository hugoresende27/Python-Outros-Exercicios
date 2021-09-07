pesos=[]

for x in range (1,6):
    peso=float(input("PESO DA PESSOA {}-->".format(x)))
    pesos.append(peso)

print ("O MAIOR peso é {}Kg e o menor é {}Kg".format(max(pesos),min(pesos)))