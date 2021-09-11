print ("\033[33;7m "+"{:=^40}".format("Programa sequência de fibonacci")+"\033[m")
valores=int(input("Quantos elementos da sequência de Fibonacci queres ver?? --> "))

i=0
num1=0
num2=1
if(valores==1):         #se só quiser 1 termo
    print (num1)
else:
    while(i<valores):   #enquanto i(contador) for menor que valores(n termos pedidos)
        print("{} | ".format(num1),end="")     #printo do proximo aqui
        proximo=num1+num2   #proximo vai ser num1 + num2
        num1=num2           #num1 passa a valer o num2
        num2=proximo        #num2 passa a valer o proximo
        i+=1            #incremento de +1 a cada ciclo na var i de inicio
print ("\033[33;7m "+"{:=^40}".format("FIM")+"\033[m")


primeiro_num=0
segundo_num=1

for num in range(0,valores):        #enquanto entre 0 e valores (input de nr de valores da seq. fibo)
    if(num<=1):                     #se num < ou igual a 1, primeiras iterações
        proximo2=num                #proximo2(var de output/print) recebe num
    else:   
        proximo2=primeiro_num+segundo_num       #senao prox2 = prim_num+seg_num
        primeiro_num=segundo_num                #prim_num=seg_num
        segundo_num=proximo2                    #seg_num=prox2
    print("{} - ".format(proximo2),end="")     #print do prox2 aqui
print ("\033[33;7m "+"{:=^40}".format("FIM")+"\033[m")