print ("\033[7m "+"{:=^40}".format("Números Primos")+"\033[m")      #numero primo divisivel apenas por 1 e por ele mesmo

n=float(input("NÚMERO --> "))
if n>1:                                 #se n maior q 1
    for i in range (2,int(n/2)+1):      #iteração de 2 a n/2
        if (n%i==0):                    #se o n é divisivel por 2 ou n/2 não é primo
            print ("NÂO É PRIMO")
            break
    else:
        print("É PRIMO")
else:
    print("NÃO É PRIMO")
