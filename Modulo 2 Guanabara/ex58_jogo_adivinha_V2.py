from random import randint
from time import sleep

n_pc=randint(0,10)
print ("-="*60)
print ("Vou pensar num número entre o e 10. Tenta adivinhar ....")
print ("-="*60)
sleep(1)

n_jog=""
tentativas=0
while (n_pc!=n_jog):
    n_jog=int(input("Em que número estou a pensar?? (0-10) --> "))
    print ("PENSANDO.....")
    sleep(0.2)
    if (n_pc==n_jog):
        print ("Você escolheu o número {} e saiu o número {} portanto GANHOU!!!".format(n_jog,n_pc))
        print ("Precisou de {} tentativas".format(tentativas))
    else:
        print("Você escolheu o número {} portanto PERDEU...".format(n_jog,n_pc))
        tentativas+=1
        print ("TENTATIVA -- {}".format(tentativas))