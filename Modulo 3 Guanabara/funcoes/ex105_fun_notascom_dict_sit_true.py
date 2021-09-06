def notas (*n,sit=False):
    """-->media de varias notas, se situacao = True mostra a situacao"""

    notas =dict()
    #notas=list()               #não preciso de lista, posso usar todas estas funções no dict,
    #for x in n:            
        #notas.append(x)        
    notas["total"]=len(n)       #uso n q é a variável do desampacotamento
    notas["maior"]=max(n)
    notas["menor"]=min(n)
    media=sum(n)/len(n)
    notas["média"]=media
    if sit:                         #igual a if sit == True
        if media>7:
            notas["situação"]="BOA"
        elif notas["média"]>=5:                 #5<media<7:           #Guanabara usa notas["media"]>=5, penso q
            notas["situação"]="RAZOÁVEL"        #como o python lê linha a linha, se >7 atribui logo BOA, se>5 fica 
        else:                                   #RAZOAVEL, senao MAU, nao preciso de 5<media<7
            notas["situação"]="MAU"
    
    
    return (notas)

resp=notas(5.5,9.5,10,6.5,sit=True)
print (resp)
print(notas(3.5,10,6.5,sit=True))
print(notas(3.5,2,6.5,2,7,4))
print (notas(5.5,2.5,8.5,sit=True))
help(notas)
