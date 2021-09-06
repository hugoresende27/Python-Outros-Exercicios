print ("\033[7m "+"{:=^40}".format("Programa Soma Impares multiplos de 3 de 1 a 500")+"\033[m")
soma=0
for x in range (1,500):
    if (x %3 == 0):
        if (x %2 !=0):
            soma+=x
            print ("Impar multiplo de 3--> {}".format(x))

print ("TOTAL {}".format(soma))  
        
        
      
