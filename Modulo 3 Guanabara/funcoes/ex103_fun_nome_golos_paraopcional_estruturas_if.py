def ficha(nome="<desconhecido>", gols=0):
    """-->Lê o nome e os golos de um jogador
    se o input for em branco tem parametros opcionas"""
    print ("o jogador %s fez %s golo(s) no campeonato" %(nome,gols))


n=str(input("Nome do jogador::"))
g=str(input("Quantos golos::"))
help(ficha)             #info da função
if g.isnumeric():       #se g é do tipo inteiro
    g = int(g)          #atribui se a g o valor de int(g)
else:
    g =0                #senão g = 0
   
if n.strip()=="":       #strip : Remove spaces at the beginning and at the end of the string:
    ficha(gols=g)
else:
    ficha(nome=n,gols=g) #se nome ok, print de tudo


