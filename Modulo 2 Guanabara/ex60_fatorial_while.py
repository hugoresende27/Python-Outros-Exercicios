num=int(input("Qual o número? --> "))
fatorial = 1            #iniciar var fatorial com valor 1
while (num>1):          #enquanto o num for maior do que 1
    print ("{} X ".format(num),end="")  #print formatado
    fatorial = fatorial*num     #fatorial recebe fatorial*num
    num-=1                      #decremento da var num -1 a cada iteração
    

print ("=",fatorial)