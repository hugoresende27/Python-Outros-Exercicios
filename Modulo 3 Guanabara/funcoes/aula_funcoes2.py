def dobra (lst):
    pos=0
    while pos<len(lst):
        lst[pos]*=2
        pos+=1


valores =[7,2,5,0,4]
dobra(valores)                  #se der print na função resulta em None, preciso fazer a função primeiro e 
print (valores)                 #só depois dar o print nos valores, agora dobrados

############## desempacotamento listas
def soma (*valores):            #desempacota lista 
    s=0                         #soma a 0
    for num in valores:         #percorre a lista valores, desempacotada
        s+=num                  #soma os valores
    print ("Somando %s temos %s" %(valores,s))      #print final da lista e da soma(s)

soma (3,1,2)
soma(2,2)