pessoas = { 
    "nome" : "Hugo", 
    "sexo" : "M", 
    "idade" : 32
                 }
pessoas["nome"] = "Zeze"            #muda valor nome para "Zeze"
pessoas["peso"] = 98.5              #adiciona chave peso com valor 98.5, não preciso de append nos dict
#del pessoas ["sexo"]                #apaga a chave e valor do sexo

print ("NOME::",pessoas["nome"] ,"tem",pessoas["idade"], "anos e é do sexo",pessoas["sexo"] )
print ("VALORES::",pessoas.values())        
print ("KEYS::",pessoas.keys())
print ("ITEMS::",pessoas.items())

for x in pessoas.values():
    print (x)

for chaves,valores in pessoas.items():
    print ("%s....%s"%(chaves,valores))

