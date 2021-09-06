estado=dict()
brasil = list()
for x in range(3):                                          #3 inputs num dicionario
    estado["UF"]=str(input("Unidade Federativa:: "))        #no fim uso uma lista (brasil) como recurso para
    estado ["SIGLA"]=str(input("Sigla do estado:: "))       #fazer um append com copy(), aqui copy()=[:]
    brasil.append(estado.copy())                            #senao fizer copy() apenas vai ficar o ultimo input

for x in brasil:                #print do dicionario numa linha
    print (x)

for x in brasil:                        #percorre a lista
    for chave, valor in x.items():      #dá print para cada elemento numa linha
        print ("o campo %s tem o valor %s" %(chave,valor))

for x in brasil:                        #outro ciclo para printar a lista
    for valor in x.values():            #primeiro vai à lista brasil, depois para cada value do x vai 
        print (valor, end=".. ")
    print()                             #dar print só no valor, tudo na mesma linha 

