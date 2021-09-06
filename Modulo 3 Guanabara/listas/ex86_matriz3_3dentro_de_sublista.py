lista=[[],[],[]]                #cria lista com 3 sublistas
for x in range (3):             #ciclo de 0 a 3 em x
    for y in range (3):         #ciclo de 0 a 3 em y
        valor = int(input("VALOR ::[%s,%s]:: " %(x,y))) #input valores e print de x e y, (0,0),(0,1),(0,2),
                                                        #                                (1,0),(1,1),(1,2),
        lista[x].append(valor)                          #append 3 a 3                    (2,0),(2,1),(2,2)
                                                        #ciclo de 3 dentro de ciclo de 3, quando y chega a 3, começa
print ("#"*30)                                          #a preencher o y, até y ser 3 tbm
for x in range(len(lista)):
    print (lista[x])
   

