############### 6 ##########
agenda= { 
    "Maria": [99887766,99887755],
    "Pedro": 92345678,
    "Patrícia": 99887711
        } 

x=input("Visualizar o contato de :")
if x in agenda:
    print(agenda[x])
else:
    print ("Contato nao existe")

print (agenda)
agenda["Pedro"]=666     #alterar valor da chave pedro para 666
print (agenda)

agenda["Hugo"]=919657338  #adicionar chave Hugo com valor 919657338
print (agenda)

print (len(agenda))     #numero de elementos no dicionario

print (agenda.keys())   #ver os nomes do dicionario

agenda.popitem()        #remover ultimo item do dicionario
print (agenda)



