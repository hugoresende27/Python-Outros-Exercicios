def fatorial(num=1,show=False):
    """->calcula o fatorial de um número
    para n o numero a ser calculado
    show mostra a conta com True
    return o valor do fatorial de um numero"""

    from time import sleep
    
    f = 1                                                #função fatorial    inicia um f em 1 para depois multiplicar
    for c in range (num,0,-1):              #faz um ciclo com contagem decrescente desde o input(num) até 0, de -1 em -1
        if show==True:                      #aqui se o show = true mostra todas as operações
            print ("%s x " %c, end =" ",flush=True)               #print de cada nr X em contagem decrescente    
            sleep(0.2)           
        f=f*c                                 #f*=c           #multiplica o f pelos num até chegar a 0
        final=f                     #para fazer o igual no fim, Guanabara fez com estrutra if c>1:print("X",end="")
    print ("=",final)                                                                    # else:print("=",end="")                            
    return f  

#fatorial(5,True)
#(fatorial(15,True))
fatorial(120)
#help(fatorial)