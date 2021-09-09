print ("\033[7m "+"{:=^40}".format("10 PASSO DE Progressão Aritmética V2")+"\033[m")

inicio=int(input("Qual o primeiro termo? --> "))
passo=int(input("P.A.? --> "))
fim=inicio+(passo*10)           #para calcular o fim, tenho de multiplicar o passo por 10 e somar o inicio

while (inicio<fim):     #enquanto inicio menor do que fim
    print ("\033[34m{}\033[m".format(inicio),end=" | ")     #print inicio
    inicio+=passo                                           #inicio é igual ao inicio mais o passo a cada iteração