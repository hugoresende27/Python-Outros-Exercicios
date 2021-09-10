from random import randint
from time import sleep

palpites=0
n_pc=randint(0,10)
print ("-="*60)
print ("Vou pensar num número entre o e 10. Tenta adivinhar ....")
print ("-="*60)
sleep(1)

acertou = False
while not acertou:
    jogador=int(input("Qual a sua aposta? --> "))
    palpites+=1
    if jogador==n_pc:
        acertou=True
    else:
        if jogador<n_pc:
            print ("é maior.....")
        elif jogador>n_pc:
            print ("é menor...")

print ("GANHOU!! em {} palpites".format(palpites))