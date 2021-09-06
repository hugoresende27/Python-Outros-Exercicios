
lista=list()
jogador=dict()


jogador["nome"]=str(input("NOME:: "))
quantas=int(input("Quantas partidas?:: "))
for x in range(quantas):
    lista.append(int(input("Quantos golos na partida %s :: "%x)))
    jogador["gols"]=lista                     
                   

jogador["total"]= sum(lista)

print("=><="*30)
print (jogador)
print("=><="*30)
for k,v in jogador.items():
    print ("O campo %s tem o valor %s" %(k,v))
print ("O jogador %s jogou %s partidas" %(jogador["nome"],quantas))
print("=><="*30)
for index,valor in  enumerate (jogador["gols"]):                #(lista): Guanabara usou enumerate dicionario[chave],
    print ("==> Na partida %s, fez %s gols" %(index,valor))     #eu tinha so enumerate a lista
print ("Foi um total de %s golos" %jogador["total"])
