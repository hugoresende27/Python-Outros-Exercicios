from datetime import date
ano_a=date.today().year

listaM=[]
listam=[]

for x in range (1,8):
    ano_nasc=int(input("ANO NASCIMENTO PESSOA NR {} --> ".format(x)))
    idade=ano_a-ano_nasc
    if (idade>=18):
        listaM.append(idade)
    else:
        listam.append(idade)
print ("Lista MAIORES:: {}".format(listaM))
print ("Lista menores:: {}".format(listam))
print ("Existem {} MAIORES e {} menores".format(len(listaM),len(listam)))