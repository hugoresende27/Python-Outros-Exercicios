lista=[]
dado=[]

for c in range(3):                          #adicionar dados com recurso a outra lista
    dado.append(str(input("NOME:: ")))      #input string do nome
    dado.append(int(input("IDADE:: ")))     #input int da idade
    lista.append(dado[:])                   #faz a cópia para a lista   [:] se não usar [:] quando dado.clear()
    dado.clear()                            #limpa a lista dado         [:] vai limpar ambas as listas

print (lista)
totmaior=totmenor=0                         #inicializa um contador para maiores e menores
for p in lista:                       #percorre lista 
    if p[1]>=21:                      #se o index [1], neste caso a idade for >) do que 21
        print ("%s é maior de idade com %s" %(p[0],p[1]))   #print do nome [0] e a idade 
        totmaior+=1                     
    else:
        print ("%s é menor de idade com %s" %(p[0],p[1]))
        totmenor+=1

print ("existem %s maiores e %s menores " %(totmaior,totmenor))