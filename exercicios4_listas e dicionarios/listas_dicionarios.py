carro = {                   #dicionario
    "marca":"Renault",      #chave / indice 0   
    "modelo": "MEganes",        #chave / indice 1
    "ano" : 2017            #....
}

print (carro)

print (carro["marca"])      #ver apenas a chave marca

print (len(carro))          #numero de items no dicionario

novodicionario = carro.copy()  #copiar um dicionario
print(novodicionario)

x=carro["modelo"]           #aceder atraves da chave
print (x)

y = carro.get("modelo")     #atraves do metodo get()    
print (y)

print (carro.keys())        #obter chaves
print (carro.values())      #obter valores


if "modelo" in carro:
    print ("SIM")

carro ["ano"]=2020      #alterar item
carro["Cor"] = "Amarelo"#adicionar item

print (carro)

carro.pop("modelo")
print (carro)

#del carro           #apaga e dá erro no print
#carro.clear()       #esvazia o dicionario

for x in carro:     #visualizar chaves
    print (x)

for x in carro.keys():      #visualizar chaves outra maneira
    print(x)

for x in carro:         #visualizar   valor
    print ("VALOR :: ",carro[x])

for x, y in carro.items():
    print (x,y)         #visualizar chave e valor