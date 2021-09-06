num =[6,6,2,9,1,8,2,3]
num[2]=3                  #mudar o index 2 para o valor 3
num.append(7)             #adicionar elemento 7 no ultimo lugar 
num.sort(reverse=True)    #ordenar inverso
num.insert (0,158)          #adicionou o elemento 158 na posição de index 0
num.pop(2)                #removeu elemento do indice 2
num.remove(2)             #removeu o primeiro 2 q apareceu

if 5 in num:
    num.remove(5)
else:
    print ("não há 5!! ")
print ("a lista tem %s elementos" %len(num))
print (num)

################################
valores =[]
valores.append(5)
valores.append(9)
valores.append(4)
print (valores)             #imprime lista com colchetes
for v in valores:
    print (v,end="")        #imprime bonito, seguido
for c,v in enumerate(valores):
    print ("\nNa posição %s encontrei o valor %s" %(c,v))       #enumerate, o c para o index e v para elemento
print ("FINAL::::::::::::::"*3)