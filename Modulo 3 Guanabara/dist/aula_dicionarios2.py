
brasil=[]

estado1={"uf": "Rio de Janeiro", 
         "sigla": "RJ"}

estado2={"uf": "São Paulo", 
         "sigla": "SP"}

brasil.append(estado1)                  #na lista criada criou 2 elementos
brasil.append(estado2)
print (brasil)                      
print (brasil[0])                   #imprime o primeiro elemento da lista [0] completo
print (brasil[0]["uf"])             #print do valor da chave uf no elemento 0
print (brasil[1]["sigla"])          #print do valor da sigla no elemento 1