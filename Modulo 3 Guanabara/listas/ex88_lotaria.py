import random
from time import sleep
print("-"*50)
print (" -- JOGO MEGA SENA --")
print("-"*50)
quantos = int(input("Quantos jogos você quer que eu sorteie?? ::"))
print ("Sorteando os %s jogos" %quantos)

jogo=[]
x=0
#for x in range (quantos):
while quantos>x:
    jogo = random.sample(range(1,60),6)
    x+=1
    jogo.sort()
    sleep(1)
    print ("jogo %s :: %s" %(x,jogo))

print("-"*50)
print (" -- BOA SORTE !! --")
print ("Hugo Resende @2021")
print("-"*50)
input()
