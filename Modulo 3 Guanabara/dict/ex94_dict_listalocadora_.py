pessoas={}
lista=list()


soma_idade=media=0

#######################################   leitura de dados
while True:
    pessoas.clear()
    pessoas["nome"]=str(input("NOME:: "))       
    while True:                                                         #ciclo para só aceitar M e F
        pessoas["sexo"]=str(input("SEXO(M/F):: ")).lower() [0]         #só lê a primeira letra 
        if pessoas["sexo"] in "mf":                                 #se sexo é M ou F
            break                                                   #break
                                #não precisa senão,repete errado até M ou F
        print("Errado, m ou f!") 
    pessoas["idade"]=int(input("IDADE:: "))
    soma_idade+=pessoas["idade"]
    lista.append(pessoas.copy())
    while True:
        res=str(input("Quer continuar(S/N)? ::")).lower()[0]
        if res in "sn":
            break
        print ("Erro, responda (S)im ou (N)ão...")
    if res == "n":
        break
########################################################################### daqui para baixo prints
print ("##"*45)
print (lista)
print ("O grupo tem %s pessoas "%len(lista))
media=(soma_idade/len(lista))
print ("A media de idade é de %.2f" %media)
print ("As mulheres do grupo são :: ",end="")
for x in lista:                                     #percorrer a lista
    if x["sexo"] == "f":          #ou in "Ff"       #se ["sexo"] na lista(x) = "f"
         print(x["nome"],end=" ")                   #print do ["nome"] na lista (x)

print ("\nlista das pessoas acima da média::")
for x in lista:                                 #percorrer a lista
    if x["idade"]>media:                        #lista locadora é usada, assim percorro a lista e depois acedo a 
        for k,v in x.items():                   #cada key pelo seu nome ["idade"] neste caso. no outro ciclo for 
            print ("   %s = %s" %(k,v),end=";") #a locadora (x) é tratada como um dict, e percorrida com o metodo 
print ("ENCERRADO")                              #.items() e depois k e v para dar print    

