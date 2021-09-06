from time import sleep

def maior(*valores):                    #desempacota quantos parametros entrarem
    maior= contador=0     
    sleep (1)                           #inicio da var maior para encontrar maior
    print ("-="*20)
    print ("Analisando os valores passados")
    for num in valores:         #percorrer a tupla valores  #percorre os num em valores, agr desempacotados 
        
        print (num,end=" ", flush=True     )        #mostra num de valores, end para ser seguido e não 1 por linha
        sleep(0.5)                                   
        if contador ==0:                            #na posicao 0, o maior é o primeiro num lido
            maior = num    
        else:
            if num > maior:                 #se num > maior q é 0 numa primeiro ciclo,
                maior=num                    #maior passa a ter o valor de num
        contador+=1                         #soma 1 ao contador para deixar de ser 0
    print ("Foram informados %s valores ao todo" %len(valores))     #comprimento da tupla
    print ("O maior valor informado foi %s ." %maior)
    
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(6)
maior()