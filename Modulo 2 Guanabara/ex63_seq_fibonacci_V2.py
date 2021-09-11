print ("\033[33;7m "+"{:=^40}".format("Programa sequência de fibonacci V2")+"\033[m")
valores=int(input("Quantos elementos da sequência de Fibonacci queres ver?? --> "))


t1=0
t2=1

print ("{} --> {}".format(t1,t2),end="")
cont=3
while (cont<=valores):
    t3 = t1+ t2
    print ("--> {} ".format(t3),end="")
    t1=t2
    t2=t3
    cont+=1                 #0 - 1 - 1 - 2 - 3 - 5 - 
                            #t1-t2 -t3
print ("-->FIM")            #   t1 -t2 -t3