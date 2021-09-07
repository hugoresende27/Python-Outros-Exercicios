print ("\033[33m "+"{:=^40}".format("Números Primos")+"\033[m")      #numero primo divisivel apenas por 1 e por ele mesmo
n=int(input("NÚMERO --> "))
total=0
for c in range (1,n+1):     #Ex: n=12  range(1,13)
    if (n%c==0):                #se o n for divisivel por Ex: 1,2,3,4,5,6,7,8,9,10,11,12
        print ("\033[33m",end=" | ")      #fica amarelo  se for divisivel
        total+=1
    else:
        print ("\033[31m",end=" | ")      #fica vermelho se não for
    print ("{}".format(c),end=" | ")

print ("\n\033[mO numero {} foi divisivel {} vezes".format(n,total))
if (total==2):                      #sabemos q o nr primo só pode ser dividido por 1 e ele mesmo, logo total==2
    print ("\033[7mÉ PRIMO\033[m")
else:                               #se o total de divisões não for 2 não é primo
    print ("\033[7mNÃO É PRIMO\033[m")