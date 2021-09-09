print ("\033[33;7m "+"{:=^40}".format("Programa soma valores 999")+"\033[m")

num=0
soma=0
contador=0
while (num!=999):
    num=int(input("Introduza um valor contador::{} (999 para sair)-->".format(contador)))
    soma+=num
    contador+=1

print ("Digitou {} números com o total somando {}".format(contador,soma-999))
print ("\033[33;7m "+"{:=^40}".format("......SAINDO......")+"\033[m")