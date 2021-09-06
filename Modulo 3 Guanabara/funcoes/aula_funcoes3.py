print (help)                #usar a funcao help para qualquer outra funcao
help (print)
help(len)

print (input.__doc__)      #imprime documentação
print (help.__doc__)

def contador (i,f,p):
    """-> faz uma contagem e mostra 
    i para inicio da contagem,
    f para o fim 
    e p para o passo da contagem, 
    aulas guanabara !!!"""
    
    while i<f:
        print (i,end=" ")
        i+=p
    print ("FIM!!")
    
contador (2,500,2)
help(contador) 

def soma (a=0,b=0,c=0):         #parametro opcional, se fizer =0, mesmo q não haja input do parametro na chamada
                                #da funçao, a funcao atribui o valor 0 e funciona na mesma 
    """funcao de somar         
    3 valores no máximo"""
    print ("A soma :::: %s" %(a+b+c))

help(soma)
soma(1,3,2)
soma(2,2)
soma()
soma (a=5,c=5)

################
def teste(b):
    global a            #vai tornar a varivel global, quando terminar a funcao a = 8 global
    a=8 
    b+=4                #var locais
    c=2
    print ("A local é %s \nB local é %s \nC local é %s" %(a,b,c))

a=5                     #var GLOBAIS
teste(a)
print ("A GLOBAL vale ",a)

def funcao ():
    n=2                 #escopo local e global
    print ("escopo local vale n",n)

n=4
print ("escopo global vale n ",n)
funcao()