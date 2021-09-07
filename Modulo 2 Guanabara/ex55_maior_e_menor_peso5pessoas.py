pesos=[]
pesomin=0
pesomax=0

for x in range (1,6):
    peso=float(input("PESO DA PESSOA {}-->".format(x)))
    pesos.append(peso)
    if x==1:            #na primeira iteracao o pesomax e pesomin vai se o primeiro (peso)
        pesomax=peso        #primeira iteracao, pesomax recebe peso e pesomin recebe peso tbm
        pesomin=peso
    else:
        if peso>pesomax:
            pesomax=peso
        if peso<pesomin:
            pesomin=peso

print ("O MAIOR peso é {}Kg e o menor é {}Kg".format(max(pesos),min(pesos)))

print ("peso minimo {}kg".format(pesomin))
print ("peso máximo {}kg".format(pesomax))