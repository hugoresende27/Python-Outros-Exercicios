from datetime import datetime
currentYear = datetime.now().year
pessoa=dict()

pessoa["nome"]=str(input("NOME:: "))
ano_nasc=int(input("ANO NASCIMENTO:: "))
pessoa["idade"]=currentYear-ano_nasc
pessoa["ct"]=int(input("CARTEIRA DE TRABALHO (0 não tem):: "))
if pessoa["ct"]!=0:                                             #para 0 vai logo para o print, se != 0 adiciona estas
    pessoa["ano_ctt"]=int(input("ANO CONTRATACAO:: "))          #chaves ao dicionário
    pessoa["salario"]=float(input("SALARIO:: "))  
    pessoa["aposentadoria"]=pessoa["ano_ctt"]+35-ano_nasc

print("=><="*30)
for k,v in pessoa.items(): 
    print ("==> %s tem o valor de %s" %(k,v))    

    
    
