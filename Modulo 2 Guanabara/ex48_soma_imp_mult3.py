print ("\033[7m "+"{:=^40}".format("Programa Soma Impares multiplos de 3 de 1 a 500")+"\033[m")
soma=0
cont=0                          #contador 
for x in range (1,501,2):       #mesmo principio do exercicio anterior. 
                                #step de 2 em 2 para obter impares
    if (x %3 ==0):              #se multiplo de 3
        cont+=1                 #total de valores impares contados
        soma+=x                 #var soma acumulador
        print ("{}".format(x),end=" | ")

print ("\033[31;43mTOTAL SOMA ::: {}  NUMEROS SOMADOS ::: {}\033[m".format(soma,cont))  
        
        
      
