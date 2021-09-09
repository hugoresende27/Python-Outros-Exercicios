print ("\033[33;7m "+"{:=^40}".format("Programa sequência de fibonacci")+"\033[m")
valores=int(input("Quantos elementos da sequência de Fibonacci queres ver?? --> "))

i=0
num1=0
num2=1

while(i<valores):
    if(i<=1):
        proximo=1           #se inicio < ou igual a 1, primeiras iterações, print do proximo que é 1
    else:
        proximo=num1+num2   #senão, proximo vai ser num1 + num2
        num1=num2           #num1 passa a valer o num2
        num2=proximo        #num2 passa a valer o proximo
    print("{}|".format(proximo),end="")     #printo do proximo aqui
    i+=1            #incremento de +1 a cada ciclo na var i de inicio

inicio=0
primeiro_num=0
segundo_num=1

for num in range(0,valores):        #enquanto entre 0 e valores (input de nr de valores da seq. fibo)
    if(num<=1):                     #se num < ou igual a 1, primeiras iterações
        proximo2=num                #proximo2(var de output/print) recebe num
    else:   
        proximo2=primeiro_num+segundo_num       #senao prox2 = prim_num+seg_num
        primeiro_num=segundo_num                #prim_num=seg_num
        segundo_num=proximo2                    #seg_num=prox2
    print("--{}--".format(proximo2),end="")     #print do prox2 aqui