
from random import shuffle

print ("#"*120)
nomes=[]

for x in range (4):
    nomes.append(input("Nome {} -->".format(x+1)))

print (nomes)
shuffle(nomes)
print ("agora a ordem será --> {}".format(nomes))
