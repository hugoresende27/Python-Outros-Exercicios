#Crie uma função que desenha uma linha de * em que o número de * entra como argumento da 
#função. O programa deverá produzir o seguinte output

def desenhar(tam):
    i=0
    for x in range(2):
        for x in range (tam+i):
            print (end="*")
        print ()
        i = i +2 
    for x in range(3):
        for x in range (tam+i):
            print (end="*")
        print ()
        i = i - 2 
   
        

desenhar(3)