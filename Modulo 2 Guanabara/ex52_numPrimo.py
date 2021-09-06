print ("\033[7m "+"{:=^40}".format("Números Primos")+"\033[m")      #numero primo divisivel apenas por 1 e por ele mesmo

n=int(input("NÚMERO --> "))
primo=False

for x in range (2,n):
    if n%x==0:
        primo=True
        break
        

if primo==True:       
    print ("{} é primo".format(n))
else:
    print ("\033[31m{} NÂO é primo".format(n))
