print ("\033[33;7m "+"{:=^40}".format("10 PASSO DE Progressão Aritmética V3")+"\033[m")

inicio=int(input("Qual o primeiro termo? --> "))
passo=int(input("P.A.? --> "))
fim=inicio+(passo*10)           #para calcular o fim, tenho de multiplicar o passo por 10 e somar o inicio

while (inicio<fim):             #enquanto inicio menor do que fim
    print ("\033[34m{}\033[m".format(inicio),end=" | ")     #print inicio
    inicio+=passo                                           #inicio é igual ao inicio mais o passo a cada iteração

controle=""
while (controle!=0):
    controle=int(input("\n\033[33mQueres mais quantos passos?? (0 para sair) --> \033[m"))
    fim2=fim+(passo*controle)
    while fim<fim2 :
        print ("\033[34m{}\033[m".format(fim),end=" | ")     #print inicio
        fim+=passo 

print ("\033[33;7m "+"{:=^40}".format("Saindo do programa Progressão Aritmética V3")+"\033[m")
