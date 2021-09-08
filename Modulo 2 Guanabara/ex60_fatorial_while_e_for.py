num=int(input("Qual o número? --> "))
fatorial = 1            #iniciar var fatorial com valor 1
while (num>1):          #enquanto o num for maior do que 1
    print ("{} X ".format(num),end="")  #print formatado
    fatorial = fatorial*num     #fatorial recebe fatorial*num
    num-=1                      #decremento da var num -1 a cada iteração
print ("=",fatorial)    


num2=int(input("Qual o número B? --> "))
factorial2=1
for i in range(1,num2 + 1):                     #com ciclo for, iniciar factorial2 a 1, for de 1 a num2+1
       factorial2 = factorial2*i                #factorial2 recebe o próprio valor X 1,2,3,4 até num2+1
print("o valor {} tem fatorial {}".format(num2,factorial2))