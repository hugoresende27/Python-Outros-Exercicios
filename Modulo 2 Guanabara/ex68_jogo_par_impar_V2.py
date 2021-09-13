from random import randint

print ("\033[7m "+"{:=^40}".format("JOGO PAR OU ÍMPAR V2")+"\033[m")
v=0
while True:
    jogador=int(input("Diga o valor:: "))
    computador=randint(0,11)
    total=jogador+computador
    tipo =" "                               #atencao ao inicio de tipo com espaço vazio
   
    while tipo not in "PI":
        tipo = str(input("Par ou Impar (P/I)? --> ")).strip().upper()[0]
    print ("Deu par" if total%2==0 else "Deu impar")
    print(f"Voce jogou {jogador} e o computador {computador} e o total foi de {total} você ",end="")
    if tipo == "P":
        if total%2==0:
            print ("venceu!!!")
            v+=1
        else:
            print ("perdeu...")
            break

    elif tipo =="I":
        if total%2!=0:
            print ("Voce venceu!!")
            v+=1
        else:
            print ("Perdeu...")
            break
    print ("vamos jogar novamente...")
print(f"Voce venceu {v} vezes")
