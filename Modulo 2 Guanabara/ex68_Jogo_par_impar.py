from random import randint

print ("\033[7m "+"{:=^40}".format("JOGO PAR OU ÍMPAR")+"\033[m")

voltas=0
vitoria=True
while vitoria:
    aposta_jog=int(input("Digite um valor ::: "))
    escolha=" "
    while escolha not in "pi":
        escolha=str(input("PAR ou IMPAR?? (P/I)--> ")).strip().lower()[0]

    aposta_pc=randint(0,10)

    resultado = aposta_pc+aposta_jog
    
    if (resultado %2==0):
        if (escolha=="p"):
            print (f"O total entre {aposta_jog} e {aposta_pc} é {resultado} e é PAR, Jogador venceu")
            vitoria=True
            voltas+=1
        else:
            print (f"O total entre {aposta_jog} e {aposta_pc} é {resultado} e é PAR, Jogador perdeu")
            vitoria=False
    elif (resultado%2!=0):
        if (escolha=="i"):
            print (f"O total entre {aposta_jog} e {aposta_pc} é {resultado} e é IMPAR, Jogador venceu")
            vitoria=True
            voltas+=1
        else:
            print (f"O total entre {aposta_jog} e {aposta_pc} é {resultado} e é IMPAR, Jogador perdeu")
            vitoria=False

print (f"FIM do jogo com {voltas} vitorias seguidas....")
