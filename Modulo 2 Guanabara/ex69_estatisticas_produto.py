print ("\033[32;7m "+"{:=^40}".format("ESTATISTICAS PRODUTO")+"\033[m")
total=0
produtos=0
mais_barato=0
while True:
    nome=str(input("Nome do produto--> "))
    preco=float(input("Preco--> "))
    total+=preco
    if preco<mais_barato:
        mais_barato=preco
        nome_mais_barato=nome
    if preco>=1000:
        produtos+=1

    sair=str(input("Quer continuar? [S/N]")).lower()[0]
    while not sair in 'sn':
        sair=str(input("Quer continuar? [S/N]--> ")).lower()[0]
    if sair=="n":
        break


print (f"Total da compra {total} Euros")
print (f"Temos {produtos} produtos custando mais de 1000 €")
print (f"O produto mais barato foi a {nome_mais_barato} e custou {mais_barato}")




print ("\033[32;7mFIM...\033[m")