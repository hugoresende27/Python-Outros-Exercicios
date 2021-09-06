todos_jog=list()

lista_golos=list()

jogador=dict()

while True:
    jogador.clear()
    jogador["nome"]=str(input("NOME:: "))
    quantas=int(input("Quantas partidas?:: "))
    lista_golos.clear()

    for x in range(quantas):
        lista_golos.append(int(input("Quantos golos na partida %s :: "%x)))
        #jogador["gols"]=lista_golos                      #ambos as linhas fazem o mesmo, Guanabara usa [:] fora do ciclo,
    jogador["gols"]=lista_golos[:]                        #eu usei uma atribuição normal dentro do ciclo

    jogador["total"]= sum(lista_golos)
    todos_jog.append(jogador.copy())            #adiciona o jogador à lista_golos criada todos_jog
    while True:                                                                 #loop para continuar , sim ou não
        res = str(input("Quer continuar(S/N)?? :: ")).upper()[0]                #apenas aceites, if res in "SN"
        if res in "SN":                 
            break                                                               #primeiro break aqui
        print ("Erro, responda (S)im ou (N)ão...")                              #se nao for S ou N dá erro e repete
    if res == "N":                                                              #até ser S ou N
        break                                                                   #se N dá o break do segundo while e acaba
                                                                            #o ciclo, se S volta ao inicio 
print("=><="*30)
#print (todos_jog)
print("=><="*30)

for x in todos_jog:                                     #mais um caso da lista_golos alocadora todos_jog, dois ciclos for
    for k,v in x.items():                               #para um print bonito, no segundo for uso .items() e k,v
        print ("O campo %s tem o valor %s" %(k,v))

print("=><="*10) 
print ("cod",end=" ")
for i in jogador.keys():
    print (f"{i:<15}",end="")   
print()          
for index,x in enumerate(todos_jog):   
    print (f"{index:>4}",end="")
    for d in x.values():
        print (f"{str(d):<15}",end="")
    print()
   
print("=><="*10)  
while True:                                     #ciclo infinito

    mostra=int(input("dados de Qual jogador?? (999 interrompe) :: "))
#    for index, x in enumerate (todos_jog):         #percorrer lista_golos com index e elemento
#        if index == mostra:                     #quando o index for igual à opção
#            print ("Mostrando dados de jogador %s" %x["nome"])
#            for j in range(len(x["gols"])):
#                print ("no jogo %s fez %s golos" %((j+1),x["gols"][j])) 
#    if mostra == 999:                                       #999 para o break
#        break
#    elif mostra > index:
#        print ("Jogador não existe!")
#############
        ### guanabaro tecnic

    if mostra==999:
        break
    if mostra >= len(todos_jog):
        print ("ERROR, não existe...")
    else:
        print ("Levantamento do jogador %s" %todos_jog[mostra]["nome"]) #mostra vai percorrer o index, uma vez q assume
        for i, g in enumerate (todos_jog[mostra]["gols"]):              #um valor int, é manipulado na lista todos_jog
            print ("No jogo %s dfez %s golos" %((i+1),g))                   #mostrando ["nome"], depois com um enumerate da 
                                #lista gols dentro da alocadora todos_jog, na posição [mostra], percorre a lista
                                #mostrando assim os golos, sendo i o index q corresponde a cada jogo