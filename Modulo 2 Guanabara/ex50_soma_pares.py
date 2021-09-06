print ("\033[7m "+"{:=^40}".format("Programa Soma pares 6 Inputs")+"\033[m")
soma=0
for x in range (1,7):
    n=int(input("Valor {} --> ".format(x)))
    if n%2==0:
        soma+=n

print ("Os seus pares somam {}".format(soma))
