from random import randint
from time import sleep
print ("\033[7m=\033[m"*100)
print ("\033[7mJOGO PEDRA TESOURA PAPEL\033[m")

lista=["pedra","tesoura","papel"]                        #   "pedra","tesoura","papel"
pc=randint(0,2)



print ("""\033[1;31mEscolha:
            0--> PEDRA
            1--> TESOURA
            2--> PAPEL""")

jog=int(input("Sua opção-->"))

print ("Pedra...")
sleep(0.5)
print ("...Tesoura....")
sleep(0.5)
print ("...Papel")
sleep(0.5)

print ("Opção do jogador \033[7m{}\033[m".format(lista[jog]))
print ("Opção do computador \033[7m{}\033[m".format(lista[pc]))

if (jog==pc):
    print ("EMPATE")
elif (jog==0 and pc==2):                                #"pedra papel"):
    print ("Computador venceu, papel embrulha pedra")
elif (jog==1 and pc==0):                                #"pedra"):
    print ("Computador venceu, pedra esmaga tesoura")
elif (jog==2 and pc==1):
    print ("Computador venceu, tesoura corta papel")
elif (jog==0 and pc==1):
    print ("Jogador venceu, pedra esmaga tesoura")
elif (jog==1 and pc==2):
    print ("Jogador venceu, tesoura corta papel")
elif (jog==2 and pc==0):
    print ("Jogador venceu, papel embrulha pedra")
else:
    print ("Opção incorrecta")