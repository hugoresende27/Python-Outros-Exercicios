print ("\033[7m "+"{:=^40}".format("Programa PARES 1 a 50")+"\033[m")

for x in range (2,51,2):            #posso começar no 2 pq 1 não é par e posso ir de 2 em 2(step) porque
                                    #assim vai fazer menos iterações
        print ("{}".format(x),end=" | ")
print ("FIM")
        