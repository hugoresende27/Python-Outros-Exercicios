print ("\033[7m "+"{:=^40}".format("Progressão Aritmética")+"\033[m")

i=int(input("Qual o primeiro termo? --> "))
p=int(input("P.A.? --> "))
f=i+(p*10)
for x in range(i,f,p):
    print ("Termo {}".format(x))