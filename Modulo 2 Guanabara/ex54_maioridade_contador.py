from datetime import date
ano_a=date.today().year     #pegar o ano atual na var ano_a, usando a lib datetime e importando apenas a date

listaM=[]
listam=[]

contadorM=0
contadorm=0

for x in range (1,8):
    ano_nasc=int(input("ANO NASCIMENTO PESSOA NR {} --> ".format(x)))
    idade=ano_a-ano_nasc
    if (idade>=18):
        listaM.append(idade)
        contadorM+=1
    else:
        listam.append(idade)
        contadorm+=1
print ("Lista MAIORES:: {}".format(listaM))
print ("Lista menores:: {}".format(listam))
print ("Existem {} MAIORES e {} menores".format(len(listaM),len(listam)))

print ("Com contadores, existem {} MAIORES ou {} menores".format(contadorM,contadorm))