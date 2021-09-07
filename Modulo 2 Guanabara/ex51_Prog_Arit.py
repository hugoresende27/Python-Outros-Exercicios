print ("\033[7m "+"{:=^40}".format("10 PASSO DE Progressão Aritmética")+"\033[m")

inicio=int(input("Qual o primeiro termo? --> "))
passo=int(input("P.A.? --> "))
fim=inicio+(passo*10)           #para calcular o fim, tenho de multiplicar o passo por 10 e somar o inicio
for x in range(inicio,fim,passo):                       #Ex. inicio = 15, passo = 5 : fim=15+(5*10);fim=15+50;fim=65
    print ("\033[34m{}\033[m".format(x),end=" | ")      #vai dar print de 15 até 60, de 5 em 5, 65 é o elemento 11