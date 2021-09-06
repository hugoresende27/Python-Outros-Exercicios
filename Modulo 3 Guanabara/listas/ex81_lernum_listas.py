res=""
lista=[]
while res!="n":
    lista.append(int(input("Digite um valor:: ")))
    res=input("Quer continuar ? [S/N]:: ").lower()
print ("Voce digitou %s elementos" %lista.count(lista))
lista.sort(reverse=True)
print ("Os valores em ordem decrescente são :: %s" %lista)
if 5 in lista:
    print ("O valor 5 faz parte da lista!!")
else:
    print ("O valor 5 não faz parte da lista !!")
###################################outra soluçao
valores=[]
while True:                                         #while True faz um ciclo infinito
    valores.append(int(input("Digite valor:: ")))
    resposta=str(input("quer continuar? (s/n)")).lower()
    if resposta in "n":                             #se a resposta de input str for um n faz break
        break
valores.sort(reverse=True)
if 5 in valores:
    print ("O valor 5 faz parte da lista!!")
else:
    print ("O valor 5 não faz parte da lista !!")
print(valores)