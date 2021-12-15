#Programa que denha um quadrado de asterisco com tamanho do lado inserido pelo utilizador.

tam = int(input("Qual o tamanho--> "))
for x in range (tam):       #controla linhas
    #print ()
    for x in range (tam):   #controla colunas
        print ("\033[0;31;42m * \033[m",end=" ")
    print ("")