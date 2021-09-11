
print ("\033[31;43m=="*10+"Programa FATORIAL"+"=="*10+"\033[m")

n=int(input("Qual o n? --> "))
print ("[WHILE GUANABARA]-->Calculando o fatorial de {}! --> ".format(n),end="")
c=n                                             #contador = numero
f=1                                             #var f(atorial) = 1
while c>0:
    print("{}".format(c),end="")
    print (" X " if c>1 else " = ",end="")      #se dentro do print
    f*=c                                        #fatorial = fatorial * contador
    c-=1                                        #contador -1
print ("{}".format(f))


num=int(input("[WHILE]-->Qual o número A? --> "))
fatorial = 1            #iniciar var fatorial com valor 1
while (num>=1):          #enquanto o num for maior ou igual a 1
    print ("{} X ".format(num),end="")  #print formatado
    fatorial = fatorial*num     #fatorial recebe fatorial*num
    num-=1                      #decremento da var num -1 a cada iteração
print ("=",fatorial)    


num2=int(input("[FOR]-->Qual o número B? --> "))
factorial2=1
for i in range(1,num2 + 1):                     #com ciclo for, iniciar factorial2 a 1, for de 1 a num2+1
       factorial2 = factorial2*i                #factorial2 recebe o próprio valor X 1,2,3,4 até num2+1
print("o valor {} tem fatorial {}".format(num2,factorial2))

from math import factorial                      #com recurso a math factorial
num2=int(input("[MATH IMPORT]-->Qual o número C? --> "))
fatorial3=factorial(num2)
print ("Fatorial C é {}".format(fatorial3))
