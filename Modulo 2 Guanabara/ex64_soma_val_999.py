print ("\033[33;7m "+"{:=^40}".format("Programa soma valores 999")+"\033[m")

num=0
soma=0
contador=0
num=int(input("Introduza um valor contador::{} (999 para sair)-->".format(contador)))
while (num!=999):
    
    soma+=num
    contador+=1
    num=int(input("Introduza um valor contador::{} (999 para sair)-->".format(contador)))

#print ("Digitou {} números com o total somando {}".format(contador-1,soma-999))
print ("Digitou {} números com o total somando {}".format(contador,soma))
print ("\033[33;7m "+"{:=^40}".format("......SAINDO......")+"\033[m")