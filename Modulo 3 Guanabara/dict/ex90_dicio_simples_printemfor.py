#aluno = {"nome":" ",                   #iniciei o dicionario assim, o guanabara apenas usou aluno=dict()
#         "media": 0,
#         "situacao":" " }

aluno=dict()        #criar o dicionario aluno

aluno["nome"]=str(input("NOME:: "))
aluno["media"]=float(input("MEDIA de %s:: "%aluno["nome"]))
if aluno["media"]>=7:
    aluno["situacao"]="Aprovado"
elif 5<aluno["media"]<10:
    aluno["situacao"]="Recuperação"
else:
    aluno["situacao"]="Reprovado"

#print ("Nome é igual a %s" %aluno["nome"])
#print ("Média é igual a %s" %aluno["media"])
#print ("Situação é igual a %s" %aluno["situacao"])

############################
for k,v in aluno.items():           #outra maneira de dar print com ciclo for
    print ("==> %s é igual a %s" %(k,v))