listaM=[]
listam=[]

for x in range (1,8):
    idade=int(input("IDADE PESSOA NR {} --> ".format(x)))
    if (idade>=18):
        listaM.append(idade)
    else:
        listam.append(idade)
print ("Lista MAIORES:: {}".format(listaM))
print ("Lista menores:: {}".format(listam))
print ("Existem {} MAIORES e {} menores".format(len(listaM),len(listam)))