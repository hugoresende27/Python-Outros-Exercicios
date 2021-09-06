import random
from time import sleep
from random import randint

jogadores= {"jogador1": randint(1,6),  #random.sample(range(1,6),1),        #com random.sample cria lista,[],
            "jogador2": randint(1,6),  #random.sample(range(1,6),1),        #randint cria um inteiro
            "jogador3": randint(1,6),  #random.sample(range(1,6),1),
            "jogador4": randint(1,6)  }#random.sample(range(1,6),1),}

print ("VALORES SORTEADOS:")
for chave,valor in jogadores.items():
    print ("o %s tirou %s no dado" % (chave,valor)   )
    sleep(1)
print ("==RANKING DOS JOGADORES==")
#print(sorted(jogadores.items(), key=lambda x: x[1],reverse=True))          #para ordenar um dict
vencedores=(sorted(jogadores.items(), key=lambda x: x[1],reverse=True))     

for key,value in enumerate (vencedores):                #para dar print, tem de ser tratado como uma lista
    print ("==>%sº lugar: %s com %s" %(key+1,value[0],value[1])) #por isso uso o enumerate
    sleep(1)




    