valores=[]
res=""

while res!="n":
    valor=int(input("Digite um valor:: "))
    
    if valor in valores:
        print ("Valor duplicado!Não vou adicionar!")
    else:
        valores.append(valor)
        print ("Valor adicionado com sucesso")

    res=input("Quer continuar? [S/N] :: ").lower()

valores.sort()

print ("Você digitou os valores:: " ,valores)
