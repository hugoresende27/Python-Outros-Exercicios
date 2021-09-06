def leiaInt(num):
    ok=False                #var para controlar o ciclo de input     
    valor=0                 #var q vai assumir o num(int)
    while True:             
        n=str(input(num))   #input como string do num
        if n.isnumeric():   #se o n(input) for númerico
            valor=int(n)    #valor assume o n como int
            ok=True         #var de controle ok passa a ser true
            
        else:     
            print ("\033[1;31m Erro!! Digite um int válido!\033[0m")  #erro com print a vermelho      
        if ok == True:      #quando var ok = True
            break           #break no ciclo
    return (valor)          #retorno do valor
                                                      

n= leiaInt("Digite um número:: ")
print ("O número q digitou foi %.0f" %n)


