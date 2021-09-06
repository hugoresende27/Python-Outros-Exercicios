
lista_fora=[[],[]]      #lista dentro de lista
valor=0
for x in range (1,8):
    
    valor=int(input("Digite o %sº valor::" %x))
    if valor %2 == 0:                       #se valor par
        lista_fora[0].append(valor)         #adiciona na primeira sublista [0]    
    else:
        lista_fora[1].append(valor)         #senao adiciona na segunda sublista [1]
     
lista_fora[0].sort()                        #ordena sublistas com o mesmo principio [0] [1]
lista_fora[1].sort()
print ("Os valores pares digitados foram ::%s" %lista_fora[0]) 
print ("Os valores IMPARES digitados foram ::%s" %lista_fora[1]) 





            


