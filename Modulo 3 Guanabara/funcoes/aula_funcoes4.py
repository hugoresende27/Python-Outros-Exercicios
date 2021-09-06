def somar (a=0,b=0,c=0):
    return a+b+c

print ("as somas valem %s %s %s" %(somar(4,5,5),somar(2,2),somar()))

def fatorial(num=1):
    f = 1                       #função fatorial    inicia um f em 1 para depois multiplicar
    for c in range (num,0,-1):  #conta de num ate 0, -1 em -1
        f=f*c   #f*=c           #multiplica o f pelos num até chegar a 0
    return f                    #retorna f, resultado de f=f*c

#print (fatorial(int  (input    ("Fatorial :: ")   )  )    )
print ("O fatorial de 5 é %s \n fatorial de 4 é %s \n fatorial de () é %s"  %(fatorial(5),fatorial(4),fatorial()))

def par(n=0):
    if n % 2 == 0:
        return True
    else :
        return False


print (par(int(input("PAR?? : "))))
num = int(input("outro nr ? ::"))
if par(num):                        #se a funcao par True, print de é par
    print ("É par")
else:
    print ("não é")                 #se é False, print não é
    