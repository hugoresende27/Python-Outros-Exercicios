lista=[]                        #lista principal
dado=[]                         #lista temporária
maior=menor=0
while True:                     #loop infinito
    dado.append(str(input("Nome::")))           #append nos temporários
    dado.append(float(input("Peso::")))
    if len(lista) == 0:                 
        maior=menor=dado[1]             #na posicao 0 de index da lista, maior e menor e input de peso iguais
    else:
        if dado[1] >= maior:            #quando o dado é maior
            maior = dado[1]             #assume a var maior
        if dado[1]<=menor:              #mesmo para o menor
            menor = dado[1]
    lista.append(dado[:])                       #[:] cria copia e não assiocia a lista
    dado.clear()

    r = (str(input("Quer continuar (S/N)? ")))
    if r in "nN":
        break
print ("Ao todo, voce cadastrou %s pessoas" %len(lista))

print ("o maior peso foi de %sKg, Peso de "%(maior),end="")
for p in lista:                                             #print de pessoas da lista sem recurso a outra lista
    if p[1] == maior:                           #ciclo for para percorrer a lista, se p[1], index das idade for == ao maior
        print (p[0],end=" ")                    #imprime o nome, index [0]
print ("\no menor peso foi de %sKg, Peso de "%(menor),end="")
for p in lista:
    if p[1]==menor:                             #o mesmo para o menor
        print(p[0],end=" ")

