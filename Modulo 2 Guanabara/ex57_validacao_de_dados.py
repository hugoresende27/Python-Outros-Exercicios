#sexo=""
sexo=str(input("\033[7mSexo? (m/f)--> \033[m")).upper().strip()[0]
while sexo not in 'MmFf':  #sexo !="M" and sexo!="F": 
    print ("\033[34;7mERRO\033[m")
    sexo=str(input("\033[7mSexo? (m/f)--> \033[m")).upper().strip()[0] #[0] faz um fatiamento para pegar apenas a primeira char
    
       
print ("sexo --> {} registado com sucesso".format(sexo))