for x in range (0,7,2):
    print ("HUGAO {}".format(x))
print ("FIM")

n=int(input("VALOR--> "))
for c in range (0,n+1):
    print (c)
print ("FIM")

i=int(input("INICIO--> "))
f=int(input("FINAL--> "))
p=int(input("PASSO--> "))

for x in range (i,f+1,p):
    print ("CONTAGEM {}".format(x))
print ("FINALE")

s=0
for c in range (0,4):
    n=int(input("N {}".format(c)))
    s+=n
print ("TOTAL{}".format(s))