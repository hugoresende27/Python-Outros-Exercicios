from random import randint
from time import sleep

n_pc=randint(0,5)
print ("-="*60)
print ("Vou pensar num número entre o e 5. Tenta adivinhar ....")
print ("-="*60)
sleep(1)

n_jog=int(input("Em que número estou a pensar?? (0-5) --> "))
print ("PENSANDO.....")
sleep(0.5)
if (n_pc==n_jog):
    print ("Você escolheu o número {} e saiu o número {} portanto GANHOU!!!".format(n_jog,n_pc))
else:
    print("Você escolheu o número {} e saiu o número {} portanto PERDEU...".format(n_jog,n_pc))